public class AudioBook extends Book {
    private double length;

    // superclass constructor
    public AudioBook(String name, int year, double length) {
        super(name, year);
        setLength(length);
    }

    private void setLength(double length) {
        this.length = length;
    }

    public double getLength() {
        return length;
    }

    public void displayInfo() {
        System.out.println(getName() + " " + getYear() + " "+ length);
    }
}
