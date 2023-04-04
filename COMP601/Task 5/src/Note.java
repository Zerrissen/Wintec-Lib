/**----------------------------------------------
 * *                   INFO
 *   Class Note defines new objects using the Note constructor.
 *   These objects can be modified with set functions,
 *   and can be retrieved with get functions.
 *---------------------------------------------**/
public class Note {
    private String pitch;
    private int duration;

    /**======================
     **        Note
     *? Constructor for Note objects
     *@param pitch String
     *@param duration int
     *@return None
     *========================**/
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
