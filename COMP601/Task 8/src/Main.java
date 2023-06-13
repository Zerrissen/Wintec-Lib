import java.util.LinkedList;
import java.util.List;

public class Main {

    public static void main(String[] args) throws Exception {
        List<Bag> bags = new LinkedList<>();
        bags.add(new Bag("blue", 12.3));
        bags.add(new Bag("red", 5.94));
        bags.add(new Bag("white", 9.86));

        BagApp bgapp = new BagApp();
        double totalCapacity = bgapp.calcTotalCapacity(bags);
        System.out.printf("Total capacity: %.2f\n", totalCapacity);
        System.out.printf("Total number of bags: %d\n", bags.size());
    }
}
