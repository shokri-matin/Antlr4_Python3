package Example;
import java.awt.GraphicsConfiguration;
import javax.swing.JFrame;

public class JFrameExample {
    public void demo(int x, int y){
        System.out.println("X= "+x+" Y="+y);
    }
    static GraphicsConfiguration gc;
    public static void main (String[] args){
        int x = 10;
        int y = 20;
        demo(x,y);
        JFrame frame = new JFrame(gc);
        frame.setTitle ("Welecome to JavaTutorial.net");
        gc.getBounds();
        gc.getDevice();
        frame.setVisible(true);
}


