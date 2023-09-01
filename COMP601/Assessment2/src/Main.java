import static java.lang.System.out;

import java.io.IOException;

public class Main {

  public static void main(String[] args) {
    TeamApp app = null;

    try {
      app = new TeamApp("data/team_data.txt");
    } catch (IOException ioe) {
      ioe.printStackTrace();
    }

    app.searchTeam();
    out.println("Number of teams: " + app.countTeams());
    out.println("Average score: " + app.getAverageScore());
  }
}
