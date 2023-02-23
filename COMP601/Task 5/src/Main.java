import java.util.List;
import java.util.LinkedList;

public class Main {
    public static void main(String[] args) {
        List<Note> notes = new LinkedList<>();
        notes.add(new Note("D", 19));
        notes.add(new Note("C", 20));
        notes.add(new Note("F", 31));
        notes.add(new Note("B", 45));
        notes.add(new Note("C", 73));
        notes.add(new Note("F", 13));
        notes.add(new Note("B", 34));
        notes.add(new Note("C", 53));
        processNotes(notes);
    }// end of main method

    public static void processNotes(List<Note> notes) {
        // print the fourth note
        System.out.println(notes.get(3));
    }
}// end of class Main