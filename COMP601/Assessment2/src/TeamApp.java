import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

class TeamApp {

  private List<Team> teams;

  public TeamApp(String filename) throws IOException {
    teams = new LinkedList<Team>();

    readTeamData(filename);
  }

  public void readTeamData(String filename) throws IOException {
    Path path = Paths.get(filename);
    List<String> lines = Files.readAllLines(path);
    for (String line : lines) {
      String[] objItem = line.split(",");
      String team_name = objItem[0];
      int group_size = Integer.parseInt(objItem[1]);
      String team_id = objItem[2];
      double score = Double.parseDouble(objItem[3]);
      teams.add(new Team(team_name, group_size, team_id, score));
    }
  }

  public int countTeams() {
    int count = 0;
    for (Team team : teams) {
      if (team.getScore() >= 50 && team.getScore() <= 90) {
        count++;
      }
    }
    return count;
  }

  public void searchTeam() {
    Scanner scanner = new Scanner(System.in);
    System.out.print("Enter ID: ");
    String userAnswer = scanner.nextLine();
    for (Team team : teams) {
      if (team.getID().equalsIgnoreCase(userAnswer)) {
        System.out.println(
          team.getName() +
          " " +
          team.getGroupSize() +
          " " +
          team.getID() +
          " " +
          team.getScore()
        );
      }
    }
  }

  public double getAverageScore() {
    double count = countTeams();
    double score = 0;
    for (Team team : teams) {
      if (team.getScore() >= 50 && team.getScore() <= 90) {
        score += team.getScore();
      }
    }

    double avgScore = (score / count);

    return avgScore;
  }
}
