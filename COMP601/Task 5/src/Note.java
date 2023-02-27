public class Note {
    private String pitch;
    private int duration;

    public Note(String pitch, int duration) {
        setPitch(pitch);
        setDuration(duration);
    }

    public void setDuration(int duration) {
        this.duration = duration;
    }

    public void setPitch(String pitch) {
        this.pitch = pitch;
    }

    public int getDuration() {
        return duration;
    }

    public String getPitch() {
        return pitch;
    }
}
