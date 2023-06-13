/**----------------------------------------------
 * *                   INFO
 *   Class Vegetable defines new objects using the Vegetable constructor.
 *   These objects can be modified with set functions,
 *   and can be retrieved with get functions.
 *   Parent class of LeafyGreen
 *---------------------------------------------**/
public class Vegetable {
    private double weight;
    private double price;

    // constructor that takes two doubles as arguments
    /**======================
     **       Vegetable
     *? Constructor for Vegetable objects
     *@param weight double
     *@param price double
     *@return None
     *========================**/
    public Vegetable(double weight, double price) {
        // call set methods
        setWeight(weight);
        setPrice(price);
    }

    // set method to set weight
    private void setWeight(double weight) {
        this.weight = weight;
    }

    // set method to set price
    private void setPrice(double price) {
        this.price = price;
    }

    // get method to get weight
    public double getWeight() {
        return weight;
    }

    // get method to get price
    public double getPrice() {
        return price;
    }

}