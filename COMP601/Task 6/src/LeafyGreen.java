public class LeafyGreen extends Vegetable {
    private String type;

    public LeafyGreen(double weight, double price, String type) {
        super(weight, price);
        setType(type);
    }

    // set method for vegetable type
    public void setType(String type) {
        this.type = type;
    }

    // get method for vegetable type
    public String getType() {
        return type;
    }
}
