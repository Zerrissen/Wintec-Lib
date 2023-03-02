public class Shape {
    private String colour;

    // constructor
    public Shape(String colour) {
        setColour(colour);
    }

    private void setColour(String colour) {
        this.colour = colour;
    }

    public String getColour() {
        return colour;
    }

    public String getShapeType() {
        return "I'm a Shape";
    }
}
