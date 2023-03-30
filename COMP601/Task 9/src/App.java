import java.io.IOException;

public class App {
    public static void main(String[] args) throws IOException {
        String dataFile = "../data/data.txt";
        System.out.println("Importing data..");
        try {
            GameApp app = new GameApp(dataFile);
            app.game();
        } catch(IOException fnf) {
            System.out.printf("File not found!");
        }
    }
}
