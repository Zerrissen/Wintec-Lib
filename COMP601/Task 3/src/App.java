import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        Scanner scanner = new Scanner(System.in);
        double score;
        // loop to ask for score between 0 and 100. if not valid, do not break.
        while (true) {
            System.out.print("Enter your score: ");
            score = scanner.nextDouble();
            if (score >= 0 && score <= 100) {
                break;
            } else {
                System.out.println("Score must be between 0 and 100");
            }
        }

        scanner.close();

        // get grade from return-value function
        System.out.println("Score " + score + " will receieve grade " + getGrade(score));

    }

    private static char getGrade(double score) {
        if (score < 50) {
            return 'D';
        } else if (score < 70) {
            return 'C';
        } else if (score < 80) {
            return 'B';
        } else {
            return 'A';
        }
    }
}
