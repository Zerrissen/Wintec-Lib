import static java.lang.System.out;

import java.util.LinkedList;
import java.util.List;

public class RecursiveArea {

    // constructor
    public RecursiveArea() {
        List<Rectangle> rectangles = new LinkedList<>();

        rectangles.add(new Rectangle(1.0, 2.0));

        rectangles.add(new Rectangle(2.0, 3.0));

        rectangles.add(new Rectangle(3.0, 4.0));

        double totalArea = getTotalRectangleArea(rectangles);

        out.printf("Total area: %.2f", totalArea);
    }

    // recursive function
    public double getTotalRectangleArea(List<Rectangle> list) {
        // Make sure list is something we can call getArea on
        // eventually this will always be 0 or null
        if (list.size() == 0 || list == null) {
            return 0;
        }
        // Get the first object in our list
        double totalArea = list.get(0).calcArea();
        // Create a new list without the object we just tested
        List<Rectangle> sublist = list.subList(1, list.size());

        // Return our total, and call our function again with our new list
        return totalArea + getTotalRectangleArea(sublist);
    }
}
