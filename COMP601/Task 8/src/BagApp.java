import java.util.List;

public class BagApp {
    public double calcTotalCapacity(List<Bag> bagList) {
        double totalCapacity = 0;

        for (Bag bag : bagList) {
            totalCapacity += bag.getCapacity();
        }
        return totalCapacity;
    }
}
