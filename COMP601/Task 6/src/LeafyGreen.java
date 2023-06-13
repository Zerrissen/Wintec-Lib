/**----------------------------------------------
 * *                   INFO
 *   Class LeafyGreen defines new objects using the LeafyGreen constructor.
 *   These objects can be modified with set functions,
 *   and can be retrieved with get functions.
 *   Child class of Vegetable
 *---------------------------------------------**/
public class LeafyGreen extends Vegetable {
    private String type;

        // constructor that takes two doubles as arguments
    /**======================
     **       LeafyGreen
     *? Constructor for LeafyGreen objects
     *@param weight double
     *@param price double
     *@param type String
     *@return None
     *========================**/
    public LeafyGreen(double weight, double price, String type) {
        super(weight, price);
        setType(type);
    }

    // set method for vegetable type
    private void setType(String type) {
        this.type = type;
    }

    // get method for vegetable type
    public String getType() {
        return type;
    }
}
