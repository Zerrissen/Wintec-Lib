public class Rectangle {

    private double length;
    private double width;

    // constructor to set length and width
    public Rectangle(double length, double width) {
        setLength(length);
        setWidth(width);
    }

    // setters and getters
    private void setLength(double length) {
        this.length = length;
    }

    private void setWidth(double width) {
        this.width = width;
    }

    public double getLength() {
        return length;
    }

    public double getWidth() {
        return width;
    }

    public double calcArea() {
        return (width * length);
    }
}
