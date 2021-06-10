import sys
from antlr4 import *
from GrammarsLexer import GrammarsLexer
from GrammarsParser import GrammarsParser
from GrammarsListener import GrammarsListener


class ExtractListener(GrammarsListener):

    # need parser to extract token stream
    def __init__(self, parser: GrammarsParser):
        self.parser = parser
        self.signatures = {}

    # get all import declaration in the source code
    def enterImportDeclaration(self, ctx):
        print('Line number: [{0}] {1}'.format(ctx.start.line, self.getAllText(ctx)))

    # decode and get text of context
    def getAllText(self, ctx):  # include hidden channel
        token_stream = ctx.parser.getTokenStream()
        lexer = token_stream.tokenSource
        input_stream = lexer.inputStream
        start = ctx.start.start
        stop = ctx.stop.stop
        return input_stream.getText(start, stop)

    # get all methods which is declared in src code
    # save all signatures method for future access
    def enterMethodDeclaration(self, ctx: GrammarsParser.MethodDeclarationContext):
        dt = 'void'  # extract data type string, None means void
        dt_ctx = ctx.datatype()
        if dt_ctx is not None:
            dt = self.getAllText(dt_ctx)
        args = self.getAllText(ctx.formalParameters())
        print('Line Number: [{0}] Method Signature: {1} {2} {3}'
              .format(ctx.start.line, dt, ctx.Identifier(), args))

        # save all signatures
        self.signatures[str(ctx.Identifier())] = str(dt) + ' ' + str(ctx.Identifier()) + ' ' + args

    # get all Local Variable which is declared in src code
    def enterLocalVariableDeclaration(self, ctx:GrammarsParser.LocalVariableDeclarationContext):
        print('Line number: [{0}] Variable Name : {1}'.format(ctx.start.line,
                                                              self.getAllText(ctx.variableDeclarators())).split('=')[0])

    # get body expression for finding some stuff such as method which is called in the method body
    def enterExpression(self, ctx: GrammarsParser.ExpressionContext):
        # get called method, they have one identifier based on grammar such as "frame.setTitle"
        # where frame is its identifier
        id = ctx.Identifier()
        explist = ctx.expressionList()
        if id:
            expr = ctx.getText().split('.')[0]
            print('Line number: [{0}] Method Called On : {1} {2}'.format(ctx.start.line, expr, id))

        # get called method, they have '()' base on grammar such as "demo(x, y)"
        if explist:
            expr = ctx.getText()
            index = expr.find('(')
            # get called method such as "frame.setTitle", they have '.' base on grammar
            if expr.find('.') > 0:
                print('Line number: [{0}] Method Called {1} Signature: Unknown'.format(ctx.start.line, expr[:index]))
            else:
                # get called method, they have '()' based on grammar such as "demo(x, y)"
                func = expr[:index]
                # search function's signature in dictionary  which we saved those in enterMethodDeclaration function
                sign = self.signatures[func]
                print('Line number: [{0}] Method Called {1} Signature: {2}'.format(ctx.start.line, func, sign))


def main(argv):
    if len(argv) > 1:
        input = FileStream(argv[1])
    else:
        input = FileStream('JFrameExample.java')

    lexer = GrammarsLexer(input)
    stream = CommonTokenStream(lexer)
    parser = GrammarsParser(stream)
    tree = parser.compilationUnit()
    listener = ExtractListener(parser)
    walker = ParseTreeWalker()
    walker.walk(listener, tree)


if __name__ == '__main__':
    main(sys.argv)
