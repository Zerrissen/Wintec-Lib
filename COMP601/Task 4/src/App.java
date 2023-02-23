import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        // get user to input comma seperated words twice, stored as two lists
        Scanner sc = new Scanner(System.in);
        List<String> list1 = new ArrayList<>();
        List<String> list2 = new ArrayList<>();

        System.out.print("Enter first list of colours: ");
        String[] list1Value = sc.nextLine().split(",");
        System.out.print("Enter second list of colours: ");
        String[] list2Value = sc.nextLine().split(",");

        sc.close();

        for (int i = 0; i < list1Value.length; i++) {
            list1.add(list1Value[i]);
        }

        for (int i = 0; i < list2Value.length; i++) {
            list2.add(list2Value[i]);
        }

        List<String> finalList = countDuplicates(list1, list2);
        System.out.println("Number of duplicates between the two lists: " + finalList.size());
        System.out.println("Duplicate colours: ");
        for (int i = 0; i < finalList.size(); i++) {
            System.out.println(finalList.get(i));
        }
    }

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
