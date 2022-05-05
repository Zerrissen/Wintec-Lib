'''
Author: Nathan Hines 21523561
Pledge of Honour: I pledge by honour that this program is solely my own work.
Description: Display formatted text using OUT inputs.
'''
from colorama import init, Fore

# Constants for colors
ERROR = Fore.RED
OUT = Fore.YELLOW
RESET = Fore.RESET
INPUT_PRINTS = [f"{OUT}Weekday hours worked: {RESET}", f"{OUT}Weekend hours worked: {RESET}", f"{OUT}Weekday pay rate: {RESET}$"]

# Function to get user input
def get_worker_values():
    inputsDone = [False, False, False]
    for i in range(len(INPUT_PRINTS)): # Only needs one while loop! Yay! Better UX!
        while sum(inputsDone) != len(inputsDone):
            if inputsDone[i] is False:
                try:
                    value = float(input(INPUT_PRINTS[i]))
                except ValueError:
                    print(f"\n{ERROR}Error: Not a number. Try again\n")
                    continue

                if i == 0: # Weekday Hours Item
                    weekdayHours = value
                    if weekdayHours > 120:
                        print(f"\n{ERROR}Error: \'{RESET}Weekday Hours{ERROR}\' cannot be greater than \'{RESET}120.{ERROR}\' Try again.\n")
                        inputsDone[i] = False
                        continue
                    elif weekdayHours < 0:
                        print(f"\n{ERROR}Error: \'{RESET}Weekday Hours{ERROR}\' cannot be less than \'{RESET}0.{ERROR}\' Try again.\n")
                        inputsDone[i] = False
                        continue
                    else:
                        inputsDone[i] = True
                    pass

                elif i == 1: # Weekend Hours Item
                    weekendHours = value
                    if weekendHours > 48:
                        print(f"\n{ERROR}Error: \'{RESET}Weekend Hours{ERROR}\' cannot be greater than \'{RESET}48.{ERROR}\' Try again.\n")
                        inputsDone[i] = False
                        continue
                    elif weekendHours < 0:
                        print(f"{ERROR}Error: \'{RESET}Weekend Hours{ERROR}\' cannot be less than \'{RESET}0.{ERROR}\' Try again.\n")
                        inputsDone[i] = False
                        continue
                    else:
                        inputsDone[i] = True
                    pass

                elif i == 2: # Weekday Pay Item
                    weekdayPayRate = value
                    if weekdayPayRate < 20:
                        print(f"\n{ERROR}Error: \'{RESET}Weekday Pay Rate{ERROR}\' cannot be less than \'{RESET}20 (current minimum wage).{ERROR}\' Try again.\n")
                        inputsDone[i] = False
                        continue
                    else:
                        inputsDone[i] = True
                    pass

                else: # In case of some random error
                    print(f"\n{ERROR}Error: Invalid input item. Try again\n")
                    continue
            else:
                break
    # Start next function
    calculate_and_display(weekdayHours, weekendHours, weekdayPayRate)

# Function to calculate owed pay and display it
def calculate_and_display(weekdaysWorked, weekendsWorked, weekdayPayRate):
    owedWeekdayPay = weekdaysWorked * weekdayPayRate
    owedWeekendPay = weekendsWorked * (weekdayPayRate * 2)
    owedTotalPay = owedWeekdayPay + owedWeekendPay

    # Print formatted output
    print(f"\n{OUT}Payment Details:")
    print(f"\tWeekday pay amount: {RESET}{owedWeekdayPay:>11.2f}\n\t{OUT}Weekend pay amount: {RESET}{owedWeekendPay:>11.2f}\n\t{OUT}Total: {RESET}{owedTotalPay:>24.2f}")

if __name__ == '__main__':
    init()
    get_worker_values()