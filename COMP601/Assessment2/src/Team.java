public class Team extends Group {

  private String ID;
  private double score;

  public Team(String name, int groupSize, String ID, double score) {
    super(name, groupSize);
    setID(ID);
    setScore(score);
  }

  // setters and getters
  private void setID(String ID) {
    this.ID = ID;
  }

  private void setScore(double score) {
    this.score = score;
  }

  public String getID() {
    return ID;
  }

  public double getScore() {
    return score;
  }
}
