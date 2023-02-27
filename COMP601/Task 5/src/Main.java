import java.util.LinkedList;
import java.util.List;

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
        // print the sum of notes duration
    }

    private static void processNotes(List<Note> notes) {
        for (Note note : notes) {
            System.out.println("The note " + note.getPitch() + " is played for " + note.getDuration() + " seconds");
        }

        System.out.println("\nTotal duration: " + notes.stream().mapToInt(Note::getDuration).sum() + " seconds");
    }
}
