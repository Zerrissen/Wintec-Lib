import java.io.IOException;

public class App {
    public static void main(String[] args) {
        String txtfile = "../data/data.txt";
        try {
            AudioBookApp app = new AudioBookApp(txtfile);
            AudioBook shortest = app.getShortestBook();
            if (shortest != null) {
                System.out.println("Shortest book:");
                shortest.displayInfo();
            }

            System.out.printf("Books published btw 2010-2020: %d\n", app.countBooks());
            app.randomBookList();

        } catch (IOException ioe) {
            System.out.printf("Perhaps missing text file: %s/%s? \n\n",
                    new App().getClass().getPackage().getName(), txtfile);
        }
    }
}
