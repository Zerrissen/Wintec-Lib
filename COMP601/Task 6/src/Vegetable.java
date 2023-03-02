public class Vegetable {
    private double weight;
    private double price;

    // constructor that takes two doubles as arguments
    public Vegetable(double weight, double price) {
        // call set methods
        setWeight(weight);
        setPrice(price);
    }

    // set method to set weight
    private void setWeight(double weight) {
        this.weight = weight;
    }

    // set method to set price
    private void setPrice(double price) {
        this.price = price;
    }

    // get method to get weight
    public double getWeight() {
        return weight;
    }

    // get method to get price
    public double getPrice() {
        return price;
    }

}