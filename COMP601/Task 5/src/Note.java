public class Note {
    String notePitch;
    int noteDuration;

    public Note(String pitch, int duration) {
        notePitch = pitch;
        noteDuration = duration;
    }

    // Get Note object pitch and duration and return it
    public String getNotePitch() {
        return notePitch;
    }

    public int getNoteDuration() {
        return noteDuration;
    }
}
