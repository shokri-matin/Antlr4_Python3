# Generated from Grammars.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GrammarsParser import GrammarsParser
else:
    from GrammarsParser import GrammarsParser

# This class defines a complete listener for a parse tree produced by GrammarsParser.
class GrammarsListener(ParseTreeListener):

    # Enter a parse tree produced by GrammarsParser#compilationUnit.
    def enterCompilationUnit(self, ctx:GrammarsParser.CompilationUnitContext):
        pass

    # Exit a parse tree produced by GrammarsParser#compilationUnit.
    def exitCompilationUnit(self, ctx:GrammarsParser.CompilationUnitContext):
        pass


    # Enter a parse tree produced by GrammarsParser#packageDeclaration.
    def enterPackageDeclaration(self, ctx:GrammarsParser.PackageDeclarationContext):
        pass

    # Exit a parse tree produced by GrammarsParser#packageDeclaration.
    def exitPackageDeclaration(self, ctx:GrammarsParser.PackageDeclarationContext):
        pass


    # Enter a parse tree produced by GrammarsParser#importDeclaration.
    def enterImportDeclaration(self, ctx:GrammarsParser.ImportDeclarationContext):
        pass

    # Exit a parse tree produced by GrammarsParser#importDeclaration.
    def exitImportDeclaration(self, ctx:GrammarsParser.ImportDeclarationContext):
        pass


    # Enter a parse tree produced by GrammarsParser#typeDeclaration.
    def enterTypeDeclaration(self, ctx:GrammarsParser.TypeDeclarationContext):
        pass

    # Exit a parse tree produced by GrammarsParser#typeDeclaration.
    def exitTypeDeclaration(self, ctx:GrammarsParser.TypeDeclarationContext):
        pass


    # Enter a parse tree produced by GrammarsParser#modifier.
    def enterModifier(self, ctx:GrammarsParser.ModifierContext):
        pass

    # Exit a parse tree produced by GrammarsParser#modifier.
    def exitModifier(self, ctx:GrammarsParser.ModifierContext):
        pass


    # Enter a parse tree produced by GrammarsParser#classOrInterfaceModifier.
    def enterClassOrInterfaceModifier(self, ctx:GrammarsParser.ClassOrInterfaceModifierContext):
        pass

    # Exit a parse tree produced by GrammarsParser#classOrInterfaceModifier.
    def exitClassOrInterfaceModifier(self, ctx:GrammarsParser.ClassOrInterfaceModifierContext):
        pass


    # Enter a parse tree produced by GrammarsParser#variableModifier.
    def enterVariableModifier(self, ctx:GrammarsParser.VariableModifierContext):
        pass

    # Exit a parse tree produced by GrammarsParser#variableModifier.
    def exitVariableModifier(self, ctx:GrammarsParser.VariableModifierContext):
        pass


    # Enter a parse tree produced by GrammarsParser#classDeclaration.
    def enterClassDeclaration(self, ctx:GrammarsParser.ClassDeclarationContext):
        pass

    # Exit a parse tree produced by GrammarsParser#classDeclaration.
    def exitClassDeclaration(self, ctx:GrammarsParser.ClassDeclarationContext):
        pass


    # Enter a parse tree produced by GrammarsParser#typeParameters.
    def enterTypeParameters(self, ctx:GrammarsParser.TypeParametersContext):
        pass

    # Exit a parse tree produced by GrammarsParser#typeParameters.
    def exitTypeParameters(self, ctx:GrammarsParser.TypeParametersContext):
        pass


    # Enter a parse tree produced by GrammarsParser#typeParameter.
    def enterTypeParameter(self, ctx:GrammarsParser.TypeParameterContext):
        pass

    # Exit a parse tree produced by GrammarsParser#typeParameter.
    def exitTypeParameter(self, ctx:GrammarsParser.TypeParameterContext):
        pass


    # Enter a parse tree produced by GrammarsParser#typeBound.
    def enterTypeBound(self, ctx:GrammarsParser.TypeBoundContext):
        pass

    # Exit a parse tree produced by GrammarsParser#typeBound.
    def exitTypeBound(self, ctx:GrammarsParser.TypeBoundContext):
        pass


    # Enter a parse tree produced by GrammarsParser#enumDeclaration.
    def enterEnumDeclaration(self, ctx:GrammarsParser.EnumDeclarationContext):
        pass

    # Exit a parse tree produced by GrammarsParser#enumDeclaration.
    def exitEnumDeclaration(self, ctx:GrammarsParser.EnumDeclarationContext):
        pass


    # Enter a parse tree produced by GrammarsParser#enumConstants.
    def enterEnumConstants(self, ctx:GrammarsParser.EnumConstantsContext):
        pass

    # Exit a parse tree produced by GrammarsParser#enumConstants.
    def exitEnumConstants(self, ctx:GrammarsParser.EnumConstantsContext):
        pass


    # Enter a parse tree produced by GrammarsParser#enumConstant.
    def enterEnumConstant(self, ctx:GrammarsParser.EnumConstantContext):
        pass

    # Exit a parse tree produced by GrammarsParser#enumConstant.
    def exitEnumConstant(self, ctx:GrammarsParser.EnumConstantContext):
        pass


    # Enter a parse tree produced by GrammarsParser#enumBodyDeclarations.
    def enterEnumBodyDeclarations(self, ctx:GrammarsParser.EnumBodyDeclarationsContext):
        pass

    # Exit a parse tree produced by GrammarsParser#enumBodyDeclarations.
    def exitEnumBodyDeclarations(self, ctx:GrammarsParser.EnumBodyDeclarationsContext):
        pass


    # Enter a parse tree produced by GrammarsParser#interfaceDeclaration.
    def enterInterfaceDeclaration(self, ctx:GrammarsParser.InterfaceDeclarationContext):
        pass

    # Exit a parse tree produced by GrammarsParser#interfaceDeclaration.
    def exitInterfaceDeclaration(self, ctx:GrammarsParser.InterfaceDeclarationContext):
        pass


    # Enter a parse tree produced by GrammarsParser#typeList.
    def enterTypeList(self, ctx:GrammarsParser.TypeListContext):
        pass

    # Exit a parse tree produced by GrammarsParser#typeList.
    def exitTypeList(self, ctx:GrammarsParser.TypeListContext):
        pass


    # Enter a parse tree produced by GrammarsParser#classBody.
    def enterClassBody(self, ctx:GrammarsParser.ClassBodyContext):
        pass

    # Exit a parse tree produced by GrammarsParser#classBody.
    def exitClassBody(self, ctx:GrammarsParser.ClassBodyContext):
        pass


    # Enter a parse tree produced by GrammarsParser#interfaceBody.
    def enterInterfaceBody(self, ctx:GrammarsParser.InterfaceBodyContext):
        pass

    # Exit a parse tree produced by GrammarsParser#interfaceBody.
    def exitInterfaceBody(self, ctx:GrammarsParser.InterfaceBodyContext):
        pass


    # Enter a parse tree produced by GrammarsParser#classBodyDeclaration.
    def enterClassBodyDeclaration(self, ctx:GrammarsParser.ClassBodyDeclarationContext):
        pass

    # Exit a parse tree produced by GrammarsParser#classBodyDeclaration.
    def exitClassBodyDeclaration(self, ctx:GrammarsParser.ClassBodyDeclarationContext):
        pass


    # Enter a parse tree produced by GrammarsParser#memberDeclaration.
    def enterMemberDeclaration(self, ctx:GrammarsParser.MemberDeclarationContext):
        pass

    # Exit a parse tree produced by GrammarsParser#memberDeclaration.
    def exitMemberDeclaration(self, ctx:GrammarsParser.MemberDeclarationContext):
        pass


    # Enter a parse tree produced by GrammarsParser#methodDeclaration.
    def enterMethodDeclaration(self, ctx:GrammarsParser.MethodDeclarationContext):
        pass

    # Exit a parse tree produced by GrammarsParser#methodDeclaration.
    def exitMethodDeclaration(self, ctx:GrammarsParser.MethodDeclarationContext):
        pass


    # Enter a parse tree produced by GrammarsParser#genericMethodDeclaration.
    def enterGenericMethodDeclaration(self, ctx:GrammarsParser.GenericMethodDeclarationContext):
        pass

    # Exit a parse tree produced by GrammarsParser#genericMethodDeclaration.
    def exitGenericMethodDeclaration(self, ctx:GrammarsParser.GenericMethodDeclarationContext):
        pass


    # Enter a parse tree produced by GrammarsParser#constructorDeclaration.
    def enterConstructorDeclaration(self, ctx:GrammarsParser.ConstructorDeclarationContext):
        pass

    # Exit a parse tree produced by GrammarsParser#constructorDeclaration.
    def exitConstructorDeclaration(self, ctx:GrammarsParser.ConstructorDeclarationContext):
        pass


    # Enter a parse tree produced by GrammarsParser#genericConstructorDeclaration.
    def enterGenericConstructorDeclaration(self, ctx:GrammarsParser.GenericConstructorDeclarationContext):
        pass

    # Exit a parse tree produced by GrammarsParser#genericConstructorDeclaration.
    def exitGenericConstructorDeclaration(self, ctx:GrammarsParser.GenericConstructorDeclarationContext):
        pass


    # Enter a parse tree produced by GrammarsParser#fieldDeclaration.
    def enterFieldDeclaration(self, ctx:GrammarsParser.FieldDeclarationContext):
        pass

    # Exit a parse tree produced by GrammarsParser#fieldDeclaration.
    def exitFieldDeclaration(self, ctx:GrammarsParser.FieldDeclarationContext):
        pass


    # Enter a parse tree produced by GrammarsParser#interfaceBodyDeclaration.
    def enterInterfaceBodyDeclaration(self, ctx:GrammarsParser.InterfaceBodyDeclarationContext):
        pass

    # Exit a parse tree produced by GrammarsParser#interfaceBodyDeclaration.
    def exitInterfaceBodyDeclaration(self, ctx:GrammarsParser.InterfaceBodyDeclarationContext):
        pass


    # Enter a parse tree produced by GrammarsParser#interfaceMemberDeclaration.
    def enterInterfaceMemberDeclaration(self, ctx:GrammarsParser.InterfaceMemberDeclarationContext):
        pass

    # Exit a parse tree produced by GrammarsParser#interfaceMemberDeclaration.
    def exitInterfaceMemberDeclaration(self, ctx:GrammarsParser.InterfaceMemberDeclarationContext):
        pass


    # Enter a parse tree produced by GrammarsParser#constDeclaration.
    def enterConstDeclaration(self, ctx:GrammarsParser.ConstDeclarationContext):
        pass

    # Exit a parse tree produced by GrammarsParser#constDeclaration.
    def exitConstDeclaration(self, ctx:GrammarsParser.ConstDeclarationContext):
        pass


    # Enter a parse tree produced by GrammarsParser#constantDeclarator.
    def enterConstantDeclarator(self, ctx:GrammarsParser.ConstantDeclaratorContext):
        pass

    # Exit a parse tree produced by GrammarsParser#constantDeclarator.
    def exitConstantDeclarator(self, ctx:GrammarsParser.ConstantDeclaratorContext):
        pass


    # Enter a parse tree produced by GrammarsParser#interfaceMethodDeclaration.
    def enterInterfaceMethodDeclaration(self, ctx:GrammarsParser.InterfaceMethodDeclarationContext):
        pass

    # Exit a parse tree produced by GrammarsParser#interfaceMethodDeclaration.
    def exitInterfaceMethodDeclaration(self, ctx:GrammarsParser.InterfaceMethodDeclarationContext):
        pass


    # Enter a parse tree produced by GrammarsParser#genericInterfaceMethodDeclaration.
    def enterGenericInterfaceMethodDeclaration(self, ctx:GrammarsParser.GenericInterfaceMethodDeclarationContext):
        pass

    # Exit a parse tree produced by GrammarsParser#genericInterfaceMethodDeclaration.
    def exitGenericInterfaceMethodDeclaration(self, ctx:GrammarsParser.GenericInterfaceMethodDeclarationContext):
        pass


    # Enter a parse tree produced by GrammarsParser#variableDeclarators.
    def enterVariableDeclarators(self, ctx:GrammarsParser.VariableDeclaratorsContext):
        pass

    # Exit a parse tree produced by GrammarsParser#variableDeclarators.
    def exitVariableDeclarators(self, ctx:GrammarsParser.VariableDeclaratorsContext):
        pass


    # Enter a parse tree produced by GrammarsParser#variableDeclarator.
    def enterVariableDeclarator(self, ctx:GrammarsParser.VariableDeclaratorContext):
        pass

    # Exit a parse tree produced by GrammarsParser#variableDeclarator.
    def exitVariableDeclarator(self, ctx:GrammarsParser.VariableDeclaratorContext):
        pass


    # Enter a parse tree produced by GrammarsParser#variableDeclaratorId.
    def enterVariableDeclaratorId(self, ctx:GrammarsParser.VariableDeclaratorIdContext):
        pass

    # Exit a parse tree produced by GrammarsParser#variableDeclaratorId.
    def exitVariableDeclaratorId(self, ctx:GrammarsParser.VariableDeclaratorIdContext):
        pass


    # Enter a parse tree produced by GrammarsParser#variableInitializer.
    def enterVariableInitializer(self, ctx:GrammarsParser.VariableInitializerContext):
        pass

    # Exit a parse tree produced by GrammarsParser#variableInitializer.
    def exitVariableInitializer(self, ctx:GrammarsParser.VariableInitializerContext):
        pass


    # Enter a parse tree produced by GrammarsParser#arrayInitializer.
    def enterArrayInitializer(self, ctx:GrammarsParser.ArrayInitializerContext):
        pass

    # Exit a parse tree produced by GrammarsParser#arrayInitializer.
    def exitArrayInitializer(self, ctx:GrammarsParser.ArrayInitializerContext):
        pass


    # Enter a parse tree produced by GrammarsParser#enumConstantName.
    def enterEnumConstantName(self, ctx:GrammarsParser.EnumConstantNameContext):
        pass

    # Exit a parse tree produced by GrammarsParser#enumConstantName.
    def exitEnumConstantName(self, ctx:GrammarsParser.EnumConstantNameContext):
        pass


    # Enter a parse tree produced by GrammarsParser#datatype.
    def enterDatatype(self, ctx:GrammarsParser.DatatypeContext):
        pass

    # Exit a parse tree produced by GrammarsParser#datatype.
    def exitDatatype(self, ctx:GrammarsParser.DatatypeContext):
        pass


    # Enter a parse tree produced by GrammarsParser#classOrInterfaceType.
    def enterClassOrInterfaceType(self, ctx:GrammarsParser.ClassOrInterfaceTypeContext):
        pass

    # Exit a parse tree produced by GrammarsParser#classOrInterfaceType.
    def exitClassOrInterfaceType(self, ctx:GrammarsParser.ClassOrInterfaceTypeContext):
        pass


    # Enter a parse tree produced by GrammarsParser#primitiveType.
    def enterPrimitiveType(self, ctx:GrammarsParser.PrimitiveTypeContext):
        pass

    # Exit a parse tree produced by GrammarsParser#primitiveType.
    def exitPrimitiveType(self, ctx:GrammarsParser.PrimitiveTypeContext):
        pass


    # Enter a parse tree produced by GrammarsParser#typeArguments.
    def enterTypeArguments(self, ctx:GrammarsParser.TypeArgumentsContext):
        pass

    # Exit a parse tree produced by GrammarsParser#typeArguments.
    def exitTypeArguments(self, ctx:GrammarsParser.TypeArgumentsContext):
        pass


    # Enter a parse tree produced by GrammarsParser#typeArgument.
    def enterTypeArgument(self, ctx:GrammarsParser.TypeArgumentContext):
        pass

    # Exit a parse tree produced by GrammarsParser#typeArgument.
    def exitTypeArgument(self, ctx:GrammarsParser.TypeArgumentContext):
        pass


    # Enter a parse tree produced by GrammarsParser#qualifiedNameList.
    def enterQualifiedNameList(self, ctx:GrammarsParser.QualifiedNameListContext):
        pass

    # Exit a parse tree produced by GrammarsParser#qualifiedNameList.
    def exitQualifiedNameList(self, ctx:GrammarsParser.QualifiedNameListContext):
        pass


    # Enter a parse tree produced by GrammarsParser#formalParameters.
    def enterFormalParameters(self, ctx:GrammarsParser.FormalParametersContext):
        pass

    # Exit a parse tree produced by GrammarsParser#formalParameters.
    def exitFormalParameters(self, ctx:GrammarsParser.FormalParametersContext):
        pass


    # Enter a parse tree produced by GrammarsParser#formalParameterList.
    def enterFormalParameterList(self, ctx:GrammarsParser.FormalParameterListContext):
        pass

    # Exit a parse tree produced by GrammarsParser#formalParameterList.
    def exitFormalParameterList(self, ctx:GrammarsParser.FormalParameterListContext):
        pass


    # Enter a parse tree produced by GrammarsParser#formalParameter.
    def enterFormalParameter(self, ctx:GrammarsParser.FormalParameterContext):
        pass

    # Exit a parse tree produced by GrammarsParser#formalParameter.
    def exitFormalParameter(self, ctx:GrammarsParser.FormalParameterContext):
        pass


    # Enter a parse tree produced by GrammarsParser#lastFormalParameter.
    def enterLastFormalParameter(self, ctx:GrammarsParser.LastFormalParameterContext):
        pass

    # Exit a parse tree produced by GrammarsParser#lastFormalParameter.
    def exitLastFormalParameter(self, ctx:GrammarsParser.LastFormalParameterContext):
        pass


    # Enter a parse tree produced by GrammarsParser#methodBody.
    def enterMethodBody(self, ctx:GrammarsParser.MethodBodyContext):
        pass

    # Exit a parse tree produced by GrammarsParser#methodBody.
    def exitMethodBody(self, ctx:GrammarsParser.MethodBodyContext):
        pass


    # Enter a parse tree produced by GrammarsParser#constructorBody.
    def enterConstructorBody(self, ctx:GrammarsParser.ConstructorBodyContext):
        pass

    # Exit a parse tree produced by GrammarsParser#constructorBody.
    def exitConstructorBody(self, ctx:GrammarsParser.ConstructorBodyContext):
        pass


    # Enter a parse tree produced by GrammarsParser#qualifiedName.
    def enterQualifiedName(self, ctx:GrammarsParser.QualifiedNameContext):
        pass

    # Exit a parse tree produced by GrammarsParser#qualifiedName.
    def exitQualifiedName(self, ctx:GrammarsParser.QualifiedNameContext):
        pass


    # Enter a parse tree produced by GrammarsParser#literal.
    def enterLiteral(self, ctx:GrammarsParser.LiteralContext):
        pass

    # Exit a parse tree produced by GrammarsParser#literal.
    def exitLiteral(self, ctx:GrammarsParser.LiteralContext):
        pass


    # Enter a parse tree produced by GrammarsParser#annotation.
    def enterAnnotation(self, ctx:GrammarsParser.AnnotationContext):
        pass

    # Exit a parse tree produced by GrammarsParser#annotation.
    def exitAnnotation(self, ctx:GrammarsParser.AnnotationContext):
        pass


    # Enter a parse tree produced by GrammarsParser#annotationName.
    def enterAnnotationName(self, ctx:GrammarsParser.AnnotationNameContext):
        pass

    # Exit a parse tree produced by GrammarsParser#annotationName.
    def exitAnnotationName(self, ctx:GrammarsParser.AnnotationNameContext):
        pass


    # Enter a parse tree produced by GrammarsParser#elementValuePairs.
    def enterElementValuePairs(self, ctx:GrammarsParser.ElementValuePairsContext):
        pass

    # Exit a parse tree produced by GrammarsParser#elementValuePairs.
    def exitElementValuePairs(self, ctx:GrammarsParser.ElementValuePairsContext):
        pass


    # Enter a parse tree produced by GrammarsParser#elementValuePair.
    def enterElementValuePair(self, ctx:GrammarsParser.ElementValuePairContext):
        pass

    # Exit a parse tree produced by GrammarsParser#elementValuePair.
    def exitElementValuePair(self, ctx:GrammarsParser.ElementValuePairContext):
        pass


    # Enter a parse tree produced by GrammarsParser#elementValue.
    def enterElementValue(self, ctx:GrammarsParser.ElementValueContext):
        pass

    # Exit a parse tree produced by GrammarsParser#elementValue.
    def exitElementValue(self, ctx:GrammarsParser.ElementValueContext):
        pass


    # Enter a parse tree produced by GrammarsParser#elementValueArrayInitializer.
    def enterElementValueArrayInitializer(self, ctx:GrammarsParser.ElementValueArrayInitializerContext):
        pass

    # Exit a parse tree produced by GrammarsParser#elementValueArrayInitializer.
    def exitElementValueArrayInitializer(self, ctx:GrammarsParser.ElementValueArrayInitializerContext):
        pass


    # Enter a parse tree produced by GrammarsParser#annotationTypeDeclaration.
    def enterAnnotationTypeDeclaration(self, ctx:GrammarsParser.AnnotationTypeDeclarationContext):
        pass

    # Exit a parse tree produced by GrammarsParser#annotationTypeDeclaration.
    def exitAnnotationTypeDeclaration(self, ctx:GrammarsParser.AnnotationTypeDeclarationContext):
        pass


    # Enter a parse tree produced by GrammarsParser#annotationTypeBody.
    def enterAnnotationTypeBody(self, ctx:GrammarsParser.AnnotationTypeBodyContext):
        pass

    # Exit a parse tree produced by GrammarsParser#annotationTypeBody.
    def exitAnnotationTypeBody(self, ctx:GrammarsParser.AnnotationTypeBodyContext):
        pass


    # Enter a parse tree produced by GrammarsParser#annotationTypeElementDeclaration.
    def enterAnnotationTypeElementDeclaration(self, ctx:GrammarsParser.AnnotationTypeElementDeclarationContext):
        pass

    # Exit a parse tree produced by GrammarsParser#annotationTypeElementDeclaration.
    def exitAnnotationTypeElementDeclaration(self, ctx:GrammarsParser.AnnotationTypeElementDeclarationContext):
        pass


    # Enter a parse tree produced by GrammarsParser#annotationTypeElementRest.
    def enterAnnotationTypeElementRest(self, ctx:GrammarsParser.AnnotationTypeElementRestContext):
        pass

    # Exit a parse tree produced by GrammarsParser#annotationTypeElementRest.
    def exitAnnotationTypeElementRest(self, ctx:GrammarsParser.AnnotationTypeElementRestContext):
        pass


    # Enter a parse tree produced by GrammarsParser#annotationMethodOrConstantRest.
    def enterAnnotationMethodOrConstantRest(self, ctx:GrammarsParser.AnnotationMethodOrConstantRestContext):
        pass

    # Exit a parse tree produced by GrammarsParser#annotationMethodOrConstantRest.
    def exitAnnotationMethodOrConstantRest(self, ctx:GrammarsParser.AnnotationMethodOrConstantRestContext):
        pass


    # Enter a parse tree produced by GrammarsParser#annotationMethodRest.
    def enterAnnotationMethodRest(self, ctx:GrammarsParser.AnnotationMethodRestContext):
        pass

    # Exit a parse tree produced by GrammarsParser#annotationMethodRest.
    def exitAnnotationMethodRest(self, ctx:GrammarsParser.AnnotationMethodRestContext):
        pass


    # Enter a parse tree produced by GrammarsParser#annotationConstantRest.
    def enterAnnotationConstantRest(self, ctx:GrammarsParser.AnnotationConstantRestContext):
        pass

    # Exit a parse tree produced by GrammarsParser#annotationConstantRest.
    def exitAnnotationConstantRest(self, ctx:GrammarsParser.AnnotationConstantRestContext):
        pass


    # Enter a parse tree produced by GrammarsParser#defaultValue.
    def enterDefaultValue(self, ctx:GrammarsParser.DefaultValueContext):
        pass

    # Exit a parse tree produced by GrammarsParser#defaultValue.
    def exitDefaultValue(self, ctx:GrammarsParser.DefaultValueContext):
        pass


    # Enter a parse tree produced by GrammarsParser#block.
    def enterBlock(self, ctx:GrammarsParser.BlockContext):
        pass

    # Exit a parse tree produced by GrammarsParser#block.
    def exitBlock(self, ctx:GrammarsParser.BlockContext):
        pass


    # Enter a parse tree produced by GrammarsParser#blockStatement.
    def enterBlockStatement(self, ctx:GrammarsParser.BlockStatementContext):
        pass

    # Exit a parse tree produced by GrammarsParser#blockStatement.
    def exitBlockStatement(self, ctx:GrammarsParser.BlockStatementContext):
        pass


    # Enter a parse tree produced by GrammarsParser#localVariableDeclarationStatement.
    def enterLocalVariableDeclarationStatement(self, ctx:GrammarsParser.LocalVariableDeclarationStatementContext):
        pass

    # Exit a parse tree produced by GrammarsParser#localVariableDeclarationStatement.
    def exitLocalVariableDeclarationStatement(self, ctx:GrammarsParser.LocalVariableDeclarationStatementContext):
        pass


    # Enter a parse tree produced by GrammarsParser#localVariableDeclaration.
    def enterLocalVariableDeclaration(self, ctx:GrammarsParser.LocalVariableDeclarationContext):
        pass

    # Exit a parse tree produced by GrammarsParser#localVariableDeclaration.
    def exitLocalVariableDeclaration(self, ctx:GrammarsParser.LocalVariableDeclarationContext):
        pass


    # Enter a parse tree produced by GrammarsParser#statement.
    def enterStatement(self, ctx:GrammarsParser.StatementContext):
        pass

    # Exit a parse tree produced by GrammarsParser#statement.
    def exitStatement(self, ctx:GrammarsParser.StatementContext):
        pass


    # Enter a parse tree produced by GrammarsParser#catchClause.
    def enterCatchClause(self, ctx:GrammarsParser.CatchClauseContext):
        pass

    # Exit a parse tree produced by GrammarsParser#catchClause.
    def exitCatchClause(self, ctx:GrammarsParser.CatchClauseContext):
        pass


    # Enter a parse tree produced by GrammarsParser#catchType.
    def enterCatchType(self, ctx:GrammarsParser.CatchTypeContext):
        pass

    # Exit a parse tree produced by GrammarsParser#catchType.
    def exitCatchType(self, ctx:GrammarsParser.CatchTypeContext):
        pass


    # Enter a parse tree produced by GrammarsParser#finallyBlock.
    def enterFinallyBlock(self, ctx:GrammarsParser.FinallyBlockContext):
        pass

    # Exit a parse tree produced by GrammarsParser#finallyBlock.
    def exitFinallyBlock(self, ctx:GrammarsParser.FinallyBlockContext):
        pass


    # Enter a parse tree produced by GrammarsParser#resourceSpecification.
    def enterResourceSpecification(self, ctx:GrammarsParser.ResourceSpecificationContext):
        pass

    # Exit a parse tree produced by GrammarsParser#resourceSpecification.
    def exitResourceSpecification(self, ctx:GrammarsParser.ResourceSpecificationContext):
        pass


    # Enter a parse tree produced by GrammarsParser#resources.
    def enterResources(self, ctx:GrammarsParser.ResourcesContext):
        pass

    # Exit a parse tree produced by GrammarsParser#resources.
    def exitResources(self, ctx:GrammarsParser.ResourcesContext):
        pass


    # Enter a parse tree produced by GrammarsParser#resource.
    def enterResource(self, ctx:GrammarsParser.ResourceContext):
        pass

    # Exit a parse tree produced by GrammarsParser#resource.
    def exitResource(self, ctx:GrammarsParser.ResourceContext):
        pass


    # Enter a parse tree produced by GrammarsParser#switchBlockStatementGroup.
    def enterSwitchBlockStatementGroup(self, ctx:GrammarsParser.SwitchBlockStatementGroupContext):
        pass

    # Exit a parse tree produced by GrammarsParser#switchBlockStatementGroup.
    def exitSwitchBlockStatementGroup(self, ctx:GrammarsParser.SwitchBlockStatementGroupContext):
        pass


    # Enter a parse tree produced by GrammarsParser#switchLabel.
    def enterSwitchLabel(self, ctx:GrammarsParser.SwitchLabelContext):
        pass

    # Exit a parse tree produced by GrammarsParser#switchLabel.
    def exitSwitchLabel(self, ctx:GrammarsParser.SwitchLabelContext):
        pass


    # Enter a parse tree produced by GrammarsParser#forControl.
    def enterForControl(self, ctx:GrammarsParser.ForControlContext):
        pass

    # Exit a parse tree produced by GrammarsParser#forControl.
    def exitForControl(self, ctx:GrammarsParser.ForControlContext):
        pass


    # Enter a parse tree produced by GrammarsParser#forInit.
    def enterForInit(self, ctx:GrammarsParser.ForInitContext):
        pass

    # Exit a parse tree produced by GrammarsParser#forInit.
    def exitForInit(self, ctx:GrammarsParser.ForInitContext):
        pass


    # Enter a parse tree produced by GrammarsParser#enhancedForControl.
    def enterEnhancedForControl(self, ctx:GrammarsParser.EnhancedForControlContext):
        pass

    # Exit a parse tree produced by GrammarsParser#enhancedForControl.
    def exitEnhancedForControl(self, ctx:GrammarsParser.EnhancedForControlContext):
        pass


    # Enter a parse tree produced by GrammarsParser#forUpdate.
    def enterForUpdate(self, ctx:GrammarsParser.ForUpdateContext):
        pass

    # Exit a parse tree produced by GrammarsParser#forUpdate.
    def exitForUpdate(self, ctx:GrammarsParser.ForUpdateContext):
        pass


    # Enter a parse tree produced by GrammarsParser#parExpression.
    def enterParExpression(self, ctx:GrammarsParser.ParExpressionContext):
        pass

    # Exit a parse tree produced by GrammarsParser#parExpression.
    def exitParExpression(self, ctx:GrammarsParser.ParExpressionContext):
        pass


    # Enter a parse tree produced by GrammarsParser#expressionList.
    def enterExpressionList(self, ctx:GrammarsParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by GrammarsParser#expressionList.
    def exitExpressionList(self, ctx:GrammarsParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by GrammarsParser#statementExpression.
    def enterStatementExpression(self, ctx:GrammarsParser.StatementExpressionContext):
        pass

    # Exit a parse tree produced by GrammarsParser#statementExpression.
    def exitStatementExpression(self, ctx:GrammarsParser.StatementExpressionContext):
        pass


    # Enter a parse tree produced by GrammarsParser#constantExpression.
    def enterConstantExpression(self, ctx:GrammarsParser.ConstantExpressionContext):
        pass

    # Exit a parse tree produced by GrammarsParser#constantExpression.
    def exitConstantExpression(self, ctx:GrammarsParser.ConstantExpressionContext):
        pass


    # Enter a parse tree produced by GrammarsParser#expression.
    def enterExpression(self, ctx:GrammarsParser.ExpressionContext):
        pass

    # Exit a parse tree produced by GrammarsParser#expression.
    def exitExpression(self, ctx:GrammarsParser.ExpressionContext):
        pass


    # Enter a parse tree produced by GrammarsParser#primary.
    def enterPrimary(self, ctx:GrammarsParser.PrimaryContext):
        pass

    # Exit a parse tree produced by GrammarsParser#primary.
    def exitPrimary(self, ctx:GrammarsParser.PrimaryContext):
        pass


    # Enter a parse tree produced by GrammarsParser#creator.
    def enterCreator(self, ctx:GrammarsParser.CreatorContext):
        pass

    # Exit a parse tree produced by GrammarsParser#creator.
    def exitCreator(self, ctx:GrammarsParser.CreatorContext):
        pass


    # Enter a parse tree produced by GrammarsParser#createdName.
    def enterCreatedName(self, ctx:GrammarsParser.CreatedNameContext):
        pass

    # Exit a parse tree produced by GrammarsParser#createdName.
    def exitCreatedName(self, ctx:GrammarsParser.CreatedNameContext):
        pass


    # Enter a parse tree produced by GrammarsParser#innerCreator.
    def enterInnerCreator(self, ctx:GrammarsParser.InnerCreatorContext):
        pass

    # Exit a parse tree produced by GrammarsParser#innerCreator.
    def exitInnerCreator(self, ctx:GrammarsParser.InnerCreatorContext):
        pass


    # Enter a parse tree produced by GrammarsParser#arrayCreatorRest.
    def enterArrayCreatorRest(self, ctx:GrammarsParser.ArrayCreatorRestContext):
        pass

    # Exit a parse tree produced by GrammarsParser#arrayCreatorRest.
    def exitArrayCreatorRest(self, ctx:GrammarsParser.ArrayCreatorRestContext):
        pass


    # Enter a parse tree produced by GrammarsParser#classCreatorRest.
    def enterClassCreatorRest(self, ctx:GrammarsParser.ClassCreatorRestContext):
        pass

    # Exit a parse tree produced by GrammarsParser#classCreatorRest.
    def exitClassCreatorRest(self, ctx:GrammarsParser.ClassCreatorRestContext):
        pass


    # Enter a parse tree produced by GrammarsParser#explicitGenericInvocation.
    def enterExplicitGenericInvocation(self, ctx:GrammarsParser.ExplicitGenericInvocationContext):
        pass

    # Exit a parse tree produced by GrammarsParser#explicitGenericInvocation.
    def exitExplicitGenericInvocation(self, ctx:GrammarsParser.ExplicitGenericInvocationContext):
        pass


    # Enter a parse tree produced by GrammarsParser#nonWildcardTypeArguments.
    def enterNonWildcardTypeArguments(self, ctx:GrammarsParser.NonWildcardTypeArgumentsContext):
        pass

    # Exit a parse tree produced by GrammarsParser#nonWildcardTypeArguments.
    def exitNonWildcardTypeArguments(self, ctx:GrammarsParser.NonWildcardTypeArgumentsContext):
        pass


    # Enter a parse tree produced by GrammarsParser#typeArgumentsOrDiamond.
    def enterTypeArgumentsOrDiamond(self, ctx:GrammarsParser.TypeArgumentsOrDiamondContext):
        pass

    # Exit a parse tree produced by GrammarsParser#typeArgumentsOrDiamond.
    def exitTypeArgumentsOrDiamond(self, ctx:GrammarsParser.TypeArgumentsOrDiamondContext):
        pass


    # Enter a parse tree produced by GrammarsParser#nonWildcardTypeArgumentsOrDiamond.
    def enterNonWildcardTypeArgumentsOrDiamond(self, ctx:GrammarsParser.NonWildcardTypeArgumentsOrDiamondContext):
        pass

    # Exit a parse tree produced by GrammarsParser#nonWildcardTypeArgumentsOrDiamond.
    def exitNonWildcardTypeArgumentsOrDiamond(self, ctx:GrammarsParser.NonWildcardTypeArgumentsOrDiamondContext):
        pass


    # Enter a parse tree produced by GrammarsParser#superSuffix.
    def enterSuperSuffix(self, ctx:GrammarsParser.SuperSuffixContext):
        pass

    # Exit a parse tree produced by GrammarsParser#superSuffix.
    def exitSuperSuffix(self, ctx:GrammarsParser.SuperSuffixContext):
        pass


    # Enter a parse tree produced by GrammarsParser#explicitGenericInvocationSuffix.
    def enterExplicitGenericInvocationSuffix(self, ctx:GrammarsParser.ExplicitGenericInvocationSuffixContext):
        pass

    # Exit a parse tree produced by GrammarsParser#explicitGenericInvocationSuffix.
    def exitExplicitGenericInvocationSuffix(self, ctx:GrammarsParser.ExplicitGenericInvocationSuffixContext):
        pass


    # Enter a parse tree produced by GrammarsParser#arguments.
    def enterArguments(self, ctx:GrammarsParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by GrammarsParser#arguments.
    def exitArguments(self, ctx:GrammarsParser.ArgumentsContext):
        pass



del GrammarsParser