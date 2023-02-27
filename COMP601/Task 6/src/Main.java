import java.util.List;
import java.util.LinkedList;

public class Main {
    public static void main(String[] args) {
        List<LeafyGreen> veges = new LinkedList<>();
        veges.add(new LeafyGreen(10, 3.5, "Cabbage"));
        veges.add(new LeafyGreen(5, 2.94, "Lettuce"));
        veges.add(new LeafyGreen(20, 5.45, "Broccoli"));
        veges.add(new LeafyGreen(7, 1.94, "Lettuce"));
        veges.add(new LeafyGreen(15, 2.8, "Lettuce"));
        veges.add(new LeafyGreen(30, 2.5, "Cabbage"));
        veges.add(new LeafyGreen(28, 4.4, "Broccoli"));
        veges.add(new LeafyGreen(20, 5.5, "Cabbage"));
        veges.add(new LeafyGreen(16, 3.9, "Broccoli"));
        veges.add(new LeafyGreen(26, 4.8, "Broccoli"));
        calculateStats(veges);
    }

    public static void calculateStats(List<LeafyGreen> veges) {
        // Calculate total price by multiplying item weight and price
        double totalPrice = 0;
        for (LeafyGreen leafyGreen : veges) {
            totalPrice += leafyGreen.getWeight() * leafyGreen.getPrice();
        }
        System.out.println("Total price: $" + totalPrice);
        // Create format strings for price and weight

        // Calculate total weight of each type
        double cabbageWeight = 0;
        double broccoliWeight = 0;
        double lettuceWeight = 0;
        double totalWeight;

        for (LeafyGreen leafyGreen : veges) {
            // for every item that matches the type, calculate the weight
            if (leafyGreen.getType().equals("Cabbage")) {
                cabbageWeight += leafyGreen.getWeight();
            } else if (leafyGreen.getType().equals("Broccoli")) {
                broccoliWeight += leafyGreen.getWeight();
            } else if (leafyGreen.getType().equals("Lettuce")) {
                lettuceWeight += leafyGreen.getWeight();
            }
        }
        // calculate the total weight
        totalWeight = cabbageWeight + broccoliWeight + lettuceWeight;
        System.out.println("Total weight: " + totalWeight + " Kg");
        System.out.println("Cabbage weight: " + cabbageWeight + " Kg");
        System.out.println("Broccoli weight: " + broccoliWeight + " Kg");
        System.out.println("Lettuce weight: " + lettuceWeight + " Kg");

    }
}