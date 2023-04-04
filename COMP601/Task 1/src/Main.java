/**----------------------------------------------
 *  *          COMMENT EXPLANATIONS
 *     Due to a comment highlighting extension in VSCode,
 *     the following characters are present in comments:
 *  ?: question/description
 *  @: parameter/argument/explanation
 *  *: important information/title
 *  !: alert/warning/error
 *  todo: Self explanatory
 *---------------------------------------------**/

/**------------------------------------------------------------------------
 * *                                ABOUT
 * @author         :  Nathan Hines (21523561)
 * @email          :  nathan@hines.net.nz
 * @repo           :  github.com/zerrissen/wintec-lib
 * @description    :  Java program to demonstrate the use of string formatting.
 * @pledge         :  I pledge by honour that this program is solely my own work.
 *------------------------------------------------------------------------**/

/*------------------ IMPORTS -----------------*/
import static java.lang.System.out;

/*------------------ ENTRY POINT -----------------*/
class Main {
    public static void main(String[] args) throws Exception {
        final String FMT = "%-20s%-10s\n"; // * Declare FMT as final and use CONSTANT naming convention

        /*------- Formatted Prints -------*/
        out.printf(FMT, "Escape sequence", "Description");
        out.println("-".repeat(42));
        out.printf(FMT, "\\n", "New Line Character");
        out.printf(FMT, "\\t", "Tab character");
        out.printf(FMT, "\\\"", "Double quote Character");
        out.printf(FMT, "\\b", "Backspace Character");
    }
}