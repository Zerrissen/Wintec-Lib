import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        // Define CONSTANTS for formatting.
        final String STR_FMT = "%-12s%-10s%-10s";
        final String NUM_FMT = "%-11.2f%-10.2f%-10.2f";
        System.out.printf("Enter circle radius: ");
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