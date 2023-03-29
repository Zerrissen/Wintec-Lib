public class Bag {
    private String colour;
    private double capacity;

    //constructor
    public Bag(String colour, double capacity) {
        setColour(colour);
        setCapacity(capacity);
    }

    private void setColour(String colour) {
        this.colour = colour;
    }

    private void setCapacity(double capacity) {
        this.capacity = capacity;
    }

    public String getColour() {
        return colour;
    }
    
    public double getCapacity() {
        return capacity;
    }
}
