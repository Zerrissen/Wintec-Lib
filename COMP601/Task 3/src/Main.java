/**------------------------------------------------------------------------
 * *                                ABOUT
 * @author         :  Nathan Hines (21523561)
 * @email          :  nathan@hines.net.nz
 * @repo           :  github.com/zerrissen/wintec-lib
 * @description    :  Find the radius, area, and perimeter of a circle.
 * @pledge         :  I pledge by honour that this program is solely my own work.
 *------------------------------------------------------------------------**/

/*------------------ IMPORTS -----------------*/
import java.util.Scanner;

/*------------------ ENTRY POINT -----------------*/
public class Main {
    public static void main(String[] args) throws Exception {
        Scanner scanner = new Scanner(System.in);
        double score;
        // * loop to ask for score between 0 and 100. If not valid, do not break.
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

        // * Get grade from return-value function getGrade
        System.out.println("Score " + score + " will receieve grade " + getGrade(score));

    }

    /**==============================================
     **                 getGrade
     *?  Takes a score and returns a grade based on score
     *@param score double  
     *@return char
     *=============================================**/
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
