/**------------------------------------------------------------------------
 * *                                ABOUT
 * @author         :  Nathan Hines (21523561)
 * @email          :  nathan@hines.net.nz
 * @repo           :  github.com/zerrissen/wintec-lib
 * @description    :  Find the radius, area, and perimeter of a circle.
 * @pledge         :  I pledge by honour that this program is solely my own work.
 *------------------------------------------------------------------------**/

/*------------------ IMPORTS -----------------*/
import java.util.Scanner;

/*------------------ ENTRY POINT -----------------*/
public class Main {
    public static void main(String[] args) throws Exception {
        // * Declare format strings as final and use CONSTANT naming convention
        final String STR_FMT = "%-12s%-10s%-10s";
        final String NUM_FMT = "%-11.2f%-10.2f%-10.2f";
        System.out.printf("Enter circle radius: ");
        // * Get user input and calculate radius, area, perimeter
        Scanner input = new Scanner(System.in);
        try {
            double radius = input.nextDouble();
            double area = Math.PI * radius * radius;
            double perimeter = 2 * Math.PI * radius;
            System.out.printf(STR_FMT, "\nRadius", "Area", "Perimeter\n");
            System.out.println("-".repeat(30));
            // format to two decimal places but with string formatting FMT
            System.out.printf(NUM_FMT, radius, area, perimeter);
        } finally {
            input.close();
        }
    }
}