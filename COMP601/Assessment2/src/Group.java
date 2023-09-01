public class Group {

  private String name;
  private int groupSize;

  // constructor to set name and groupSize
  public Group(String name, int groupSize) {
    setName(name);
    setGroupSize(groupSize);
  }

  // setters and getters
  private void setName(String name) {
    this.name = name;
  }

  private void setGroupSize(int groupSize) {
    this.groupSize = groupSize;
  }

  public String getName() {
    return name;
  }

  public int getGroupSize() {
    return groupSize;
  }
}
