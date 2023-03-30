public class Country {
    private String name;
    private String capital;
    private int population;

    public Country(String name, String capital, int population) {
        setName(name);
        setCapital(capital);
        setPopulation(population);
    }

    private void setName(String name) {
        this.name = name;
    }

    private void setCapital(String capital) {
        this.capital = capital;
    }

    private void setPopulation(int population) {
        this.population = population;
    }

    public String getName() {
        return name;
    }

    public String getCapital() {
        return capital;
    }

    public int getPopulation() {
        return population;
    }
}
