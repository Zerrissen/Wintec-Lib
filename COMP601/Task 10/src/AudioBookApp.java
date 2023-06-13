import java.io.IOException;
import java.util.List;
import java.util.LinkedList;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.Files;
import java.util.concurrent.ThreadLocalRandom;

public class AudioBookApp {
    private List<AudioBook> bookList;

    public List<AudioBook> getBookList() {
        return bookList;
    }

    public AudioBookApp(String filename) throws IOException {
        bookList = new LinkedList<>();
        readData(filename);
    }

    public void readData(String filename) throws IOException {
        Path path = Paths.get(filename);
        List<String> lines = Files.readAllLines(path);
        for (String line : lines) {
            String[] objItem = line.split(",");
            String name = objItem[0];
            int year = Integer.parseInt(objItem[1]);
            double length = Double.parseDouble(objItem[2]);
            bookList.add(new AudioBook(name, year, length));
        }
    }

    public AudioBook getShortestBook() {
        double length = bookList.get(0).getLength();
        AudioBook shortestBook = bookList.get(0);
        for (AudioBook book : bookList) {
            if (length > book.getLength()) {
                shortestBook = book;
            }
        }
        return shortestBook;
    }

    public int countBooks() {
        int count = 0;
        for (AudioBook book : bookList) {
            if (book.getYear() > 2010 && book.getYear() < 2020) {
                count ++;
            }
        }
        return count;
    }

    public void randomBookList() {

        List<AudioBook> b1;
        b1 = new LinkedList<>();
        List<AudioBook> b2;
        b2 = new LinkedList<>();
        List<AudioBook> b3;
        b3 = new LinkedList<>();

        for (AudioBook book : bookList) {
            int randomInt = ThreadLocalRandom.current().nextInt(1,3);
            if (randomInt == 1) {
                b1.add(book);
            } else if (randomInt == 2) {
                b2.add(book);
            } else {
                b3.add(book);
            }
        }

        System.out.println("\nBooks in list #1: " + b1.size());
        for (AudioBook book : b1) {
            book.displayInfo();
        }
        System.out.println("\nBooks in list #2: " + b2.size());
        for (AudioBook book : b2) {
            book.displayInfo();
        }
        System.out.println("\nBooks in list #3: " + b3.size());
        for (AudioBook book : b3) {
            book.displayInfo();
        }
    }
}
