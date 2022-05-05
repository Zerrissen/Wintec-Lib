'''
Author: Nathan Hines 21523561
Pledge of Honour: I pledge by honour that this program is solely my own work.
Description: Determine grocery discount eligibility
'''

from colorama import init, Fore

# Constants for colors
ERROR = Fore.RED
OUT = Fore.YELLOW
RESET = Fore.RESET
INPUT_PRINTS = [f"{OUT}Enter item price: {RESET}$", f"{OUT}Enter quantity of item: {RESET}"]

# Function used to get users product values
def get_product_info():
    inputsDone = [False, False]
    for i in enumerate(INPUT_PRINTS):
        while sum(inputsDone) != len(inputsDone):
            if inputsDone[i] is False:
                try: # Checks values of BOTH inputs with only one loop! Yay!
                    value = float(input(INPUT_PRINTS[i]))
                except ValueError:
                    print(f"\n{ERROR}Error: Not a number. Try again\n")
                    continue
                if i == 0: # Price item
                    price = value
                    if price < 0:
                        print(f"\n{ERROR}Error: \'{RESET}Price{ERROR}\' cannot be less than \'{RESET}0.{ERROR}\' Try again.\n")
                        inputsDone[i] = False
                        continue
                    else:
                        inputsDone[i] = True
                        pass
                elif i == 1: # Quantity item
                    quantity = value
                    if quantity < 0:
                        print(f"\n{ERROR}Error: \'{RESET}Quantity{ERROR}\' cannot be less than \'{RESET}0.{ERROR}\' Try again.\n")
                        inputsDone[i] = False
                        continue
                    else:
                        inputsDone[i] = True
                        pass
                else: # In case of some random error
                    print(f"\n{ERROR}Error: Unknown Error. Try again\n")
                    continue
            else:
                break
    get_customer_info(price, quantity) # Passes these parameters so calculation can see them without making them global.

# Function to determine information about the user.
def get_customer_info(price, quantity):
    claimed = False
    while True:
        try: # Checks values of input and validates it.
            customerClaimedDiscount = input(f"{OUT}Have you claimed our discount before? (y/n): {RESET}")
            pass
        except ValueError:
            print(f"\n{ERROR}Error: Invalid input. Try again.\n")
            continue
        if customerClaimedDiscount in ("y", "Y"):
            claimed = True
            break
        elif customerClaimedDiscount in ("n", "N"):
            claimed = False
            break
        else: # In case of some random error
            print("\n{ERROR}Error: Unknown Error. Try again.\n")
            continue
    calculate_and_output(price, quantity, claimed) # Passes parameters again to final function

# Function calculates eligibility using previous given input.
def calculate_and_output(price, quantity, claimed):
    totalPriceBeforeDiscount = price * quantity

    if claimed is True and totalPriceBeforeDiscount < 500:
        print(f"\n{OUT}Total price: {RESET}${totalPriceBeforeDiscount:.2f} \n{OUT}Claimed discount: {RESET}" + str(claimed))
        print(f"\n{OUT}You are eligible for the discount.")
    else:
        print(f"\n{OUT}Total price: {RESET}${totalPriceBeforeDiscount:.2f}\n{OUT}Claimed discount: {RESET}" + str(claimed))
        print(F"\n{OUT}You are not eligible for the discount.")

# Driver code in the event that the program is used as a module.
if __name__ == '__main__':
    init()
    get_product_info()