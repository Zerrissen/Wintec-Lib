/**------------------------------------------------------------------------
 * *                                ABOUT
 * @author         :  Nathan Hines (21523561)
 * @email          :  nathan@hines.net.nz
 * @repo           :  github.com/zerrissen/wintec-lib
 * @description    :  Demonstrate polymorphism
 * @pledge         :  I pledge by honour that this program is solely my own work.
 *------------------------------------------------------------------------**/

/*------------------ IMPORTS -----------------*/
import java.util.List;
import java.util.LinkedList;

/*------------------ ENTRY POINT -----------------*/
public class Main {
    public static void main(String[] args) {
        List<Shape> shapes = new LinkedList<>();
        shapes.add(new Shape("white"));
        shapes.add(new Rectangle("red", 10, 6));
        shapes.add(new Rectangle("black", 20, 9));
        shapes.add(new Shape("orange"));

        // produces output part 1
        showShapeNames(shapes);
        Rectangle[] rectangleArray1 = {
                new Rectangle("white", 4, 3),
                new Rectangle("red", 9, 5),
                new Rectangle("purple", 3, 6),
                new Rectangle("orange", 15, 10),
                new Rectangle("black", 4, 14),
        };
        Rectangle[] rectangleArray2 = {
                new Rectangle("pink", 3, 4),
                new Rectangle("red", 10, 2),
                new Rectangle("white", 8, 5),
                new Rectangle("blue", 14, 4),
                new Rectangle("bindle", 10, 15),
        };

        // produces output part 2
        countOverlapRectangles(rectangleArray1, rectangleArray2);
    }

    public static void showShapeNames(List<Shape> shapes) {
        for (Shape shape : shapes) {
            System.out.println(shape.getShapeType());
        }
    }

    public static void countOverlapRectangles(Rectangle[] group1, Rectangle[] group2) {
        int colourOverlap = 0;
        int perimeterOverlap = 0;
        for (Rectangle r1 : group1) {
            for (Rectangle r2 : group2) {
                if (r1.getColour() == r2.getColour()) {
                    colourOverlap++;
                }
                if (r1.getPerimeter() == r2.getPerimeter()) {
                    perimeterOverlap++;
                }
            }
        }

        System.out.println("There are " + colourOverlap + " Rectangles with the same colour.");
        System.out.println("There are " + perimeterOverlap + " Rectangles with the same perimeter.");

    }
}