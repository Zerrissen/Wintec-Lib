/**------------------------------------------------------------------------
 * *                                ABOUT
 * @author         :  Nathan Hines (21523561)
 * @email          :  nathan@hines.net.nz
 * @repo           :  github.com/zerrissen/wintec-lib
 * @description    :  Demonstrate the use of classes and get/set methods.
 * @pledge         :  I pledge by honour that this program is solely my own work.
 *------------------------------------------------------------------------**/

/*------------------ IMPORTS -----------------*/
import java.util.LinkedList;
import java.util.List;

/*------------------ ENTRY POINT -----------------*/
public class Main {
    public static void main(String[] args) {
        // * Create a list of object type Note. See Note.java
        List<Note> notes = new LinkedList<>();
        // * Add a series of notes with different values to a list.
        notes.add(new Note("D", 19));
        notes.add(new Note("C", 20));
        notes.add(new Note("F", 31));
        notes.add(new Note("B", 45));
        notes.add(new Note("C", 73));
        notes.add(new Note("F", 13));
        notes.add(new Note("B", 34));
        notes.add(new Note("C", 53));

        // * Call the processNotes method.
        processNotes(notes);
    }

    /**==============================================
     **                processNotes
     * ? Iterates list, calls Note object get methods and prints the results
     * @param List<Note> notes
     * @return None
     *=============================================**/
    private static void processNotes(List<Note> notes) {
        for (Note note : notes) {
            System.out.println("The note " + note.getPitch() + " is played for " + note.getDuration() + " seconds");
        }

        System.out.println("\nTotal duration: " + notes.stream().mapToInt(Note::getDuration).sum() + " seconds");
    }
}
