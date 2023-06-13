import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.concurrent.ThreadLocalRandom;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

public class GameApp {
    Scanner scanner = new Scanner(System.in);
    private List<Country> countryList;

    public GameApp(String dataFile) throws IOException {
        readData(dataFile);
    }

    private void readData(String fileName) throws IOException {
        countryList = new LinkedList<>();
        Path path = Paths.get(fileName);
        List<String> lines = Files.readAllLines(path);
        for (String line : lines) {
            String[] objItem = line.split(",");
            String country = objItem[0];
            String capital = objItem[1];
            int population = Integer.parseInt(objItem[2]);
            countryList.add(new Country(country, capital, population));
        }
    }

    public void game() {
        int lastInt = -1; // * Assigned as negative here to prevent it interfering with first time
                          // * selection.
        while (true) {
            int randomInt = ThreadLocalRandom.current().nextInt(0, countryList.size());
            int triesLeft = 3;
            if (randomInt == lastInt) { // * Used to make sure the user doesn't get the same country twice in a row.
                continue;
            }
            lastInt = randomInt;
            Country randomObj = countryList.get(randomInt);
            String capitalAnswer = randomObj.getCapital();
            String countryName = randomObj.getName();
            while (triesLeft > 0) {
                triesLeft--; // * Start of a new try, so subtract 1
                System.out.print("What is the capital of " + countryName + "?: ");
                String userAnswer = scanner.nextLine();
                if (userAnswer.equalsIgnoreCase(capitalAnswer)) {
                    System.out.println("Correct! " + countryName + " is a country with a pop. of "
                            + randomObj.getPopulation() + " million.");
                    break;
                } else if (triesLeft == 0) {
                    System.out.println("Game over! All tries used.");
                } else {
                    System.out.println("Wrong.. Try again! (" + triesLeft + " tries remaining)");
                }
            }
            System.out.print("Play again? (Y/N): ");
            String userContinue = scanner.nextLine();
            if (userContinue.equalsIgnoreCase("y")) { // * Used y here so anything else is "No"
                continue;
            }
            break;
        }
    }
}
