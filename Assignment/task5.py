'''
Author: Nathan Hines 21523561
Pledge of Honour: I pledge by honour that this program is solely my own work.
Description: Determine grocery discount eligibility
'''

def get_product_info(): # Function used to get users product values
    validPrice = []
    validQuantity = []
    priceDone = False
    quantityDone = False
    while True:
        try: # Checks values of BOTH inputs with only one loop! Yay!
            if priceDone == False:
                itemPrice = float(input("Enter item price: $"))
                validPrice.append(itemPrice)
                priceDone = True
            if quantityDone == False:
                itemQuantity = int(input("Enter quantity of item: "))
                validQuantity.append(itemQuantity)
                quantityDone = True
            pass
        except ValueError:
            print("\nError: Invalid input. Try again.\n")
            continue
        if priceDone == False or quantityDone == False:
            continue
        else:
            break
    #print("Done!") # Used for testing purposes
    #print(validPrice, validQuantity) # Used for testing purposes
    get_customer_info(validPrice, validQuantity) # Passes these parameters so calculation can see them without making them global.

def get_customer_info(validPrice, validQuantity): # Function to determine information about the user.
    claimed = False
    while True:
        try: # Checks values of input and validates it.
            customerClaimedDiscount = input("Have you claimed our discount before? (y/n): ")
            pass
        except ValueError:
            print("\nError: Invalid input. Try again.\n")
            continue
        if customerClaimedDiscount == "y" or customerClaimedDiscount == "Y":
            claimed = True
            break
        elif customerClaimedDiscount == "n" or customerClaimedDiscount == "N":
            claimed = False
            break
        else:
            print("\nError: Invalid input. Try again.\n")
            continue
    calculate_and_output(validPrice, validQuantity, claimed)

def calculate_and_output(validPrice, validQuantity, claimed): # Function calculates eligibility using previous given input.
    totalPriceBeforeDiscount = validPrice[0] * validQuantity[0]
    if claimed == True and totalPriceBeforeDiscount < 500:
        print(f"\nTotal price: ${totalPriceBeforeDiscount:.2f} \nClaimed discount: " + str(claimed))
        print("\nYou are eligible for the discount.")
    else:
        print(f"\nTotal price: ${totalPriceBeforeDiscount:.2f}\nClaimed discount: " + str(claimed))
        print("\nYou are not eligible for the discount.")

if __name__ == '__main__': # Driver code in the event that the program is used as a module.
    get_product_info()