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

    public void game(){
        int randomInt = ThreadLocalRandom.current().nextInt(0,countryList.size());
        Country randomObj = countryList.get(randomInt);
        String capitalAnswer = randomObj.getCapital();
        String countryName = randomObj.getName();
        System.out.println("What is the capital of " + countryName + ": ");
        String userAnswer = scanner.nextLine();
        if (userAnswer.equals(capitalAnswer)) {
            System.out.println("Correct! " + countryName + " is a country of " + randomObj.getPopulation() +" million.");
        } else {
            System.out.println("Wrong..");
        }
        System.out.println("Continue? (Y/N): ");
        String userContinue = scanner.nextLine();
        if (userContinue.equalsIgnoreCase("n")) {
            return;
        }
    }
}
