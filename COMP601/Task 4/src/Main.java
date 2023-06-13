/**------------------------------------------------------------------------
 * *                                ABOUT
 * @author         :  Nathan Hines (21523561)
 * @email          :  nathan@hines.net.nz
 * @repo           :  github.com/zerrissen/wintec-lib
 * @description    :  Take user input and iterate through two lists to find duplicate values.
 * @pledge         :  I pledge by honour that this program is solely my own work.
 *------------------------------------------------------------------------**/

/*------------------ IMPORTS -----------------*/
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/*------------------ ENTRY POINT -----------------*/
public class Main {
    public static void main(String[] args) throws Exception {
        // *Get user to input comma seperated words twice, stored as two lists
        Scanner sc = new Scanner(System.in);
        List<String> list1 = new ArrayList<>();
        List<String> list2 = new ArrayList<>();

        System.out.print("Enter first list of colours seperated by comma (,): ");
        String[] list1Value = sc.nextLine().split(",");
        System.out.print("Enter second list of colours seperated by comma (,): ");
        String[] list2Value = sc.nextLine().split(",");

        sc.close();

        // * Iterate through String Arrays and add values to the two lists
        for (int i = 0; i < list1Value.length; i++) {
            list1.add(list1Value[i]);
        }

        for (int i = 0; i < list2Value.length; i++) {
            list2.add(list2Value[i]);
        }

        // * Call countDuplicates to count the number of duplicates in the two lists &
        // * print.
        List<String> finalList = countDuplicates(list1, list2);
        System.out.println("Number of duplicates between the two lists: " + finalList.size());
        System.out.println("Duplicate colours: ");

        // * Iterate through the finalList and print each value
        for (int i = 0; i < finalList.size(); i++) {
            System.out.println(finalList.get(i));
        }
    }

    /**
     * ==============================================
     ** countDuplicates
     * ? Iterates the two lists and counts the duplicate items.
     * 
     * @param List<String> list1
     * @param List<String> list2
     * @return List<String>
     *         =============================================
     **/
    private static List<String> countDuplicates(List<String> list1, List<String> list2) throws Exception {
        List<String> finalList = new ArrayList<>();
        for (int i = 0; i < list1.size(); i++) {
            for (int j = 0; j < list2.size(); j++) {
                if (list1.get(i).equals(list2.get(j))) {
                    finalList.add(list1.get(i));
                }
            }
        }

        return finalList;
    }
}
