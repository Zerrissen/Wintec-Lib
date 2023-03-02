public class Rectangle extends Shape {
    private double width;
    private double height;

    // superclass constructor to set height and width and colour
    public Rectangle(String colour, double width, double height) {
        super(colour);
        setWidth(width);
        setHeight(height);
    }

    private void setWidth(double width) {
        this.width = width;

    }

    private void setHeight(double height) {
        this.height = height;
    }

    public double getWidth() {
        return width;
    }

    public double getHeight() {
        return height;
    }

    public double getPerimeter() {
        return 2 * (width + height);
    }

    // override method for getShapeType()
    @Override
    public String getShapeType() {
        return "I'm a Rectangle";
    }

}
