public class Book {
    private String name;
    private int year;

    public Book(String name, int year) {
        setName(name);
        setYear(year);
    }

    private void setName(String name) {
        this.name = name;
    }

    private void setYear(int year) {
        this.year = year;
    }

    public String getName() {
        return name;
    }

    public int getYear() {
        return year;
    }
}
