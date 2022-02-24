'''
Author: Nathan Hines 21523561
Pledge of Honour: I pledge by honour that this program is solely my own work.
Description: Display formatted text using user inputs.
'''

from calendar import weekday


def get_worker_values():
    while True:
        try:
            weekdaysWorked = float(input("Number of weekday hours worked: "))
            weekendsWorked = float(input("Number of weekend hours worked: "))
            weekdayPayRate = float(input("Weekday pay rate: "))
            weekendPayRate = weekdayPayRate * 2
        except ValueError:
            print("\nError: Invalid input. Try again.\n")
            continue
        if weekdaysWorked < 0 or weekendsWorked < 0 or weekdayPayRate < 0 or weekendPayRate < 0:
            print("\nError: Values cannot be negative. Try Again.\n")
            continue
        elif weekdaysWorked > 120 and weekendsWorked > 48:
            print("\nError: Too many weekday and weekend hours. Try again.\n")
        elif weekdaysWorked > 120:
            print("\nError: Too many weekday hours. Try again.\n")
        elif weekendsWorked > 48:
            print("\nError: Too many weekend hours. Try again.\n")
        else:
            break
    calculate_and_display(weekdaysWorked, weekendsWorked, weekdayPayRate, weekendPayRate)

def calculate_and_display(weekdaysWorked, weekendsWorked, weekdayPayRate, weekendPayRate):
    weekdayPay = weekdaysWorked * weekdayPayRate
    weekendPay = weekendsWorked * weekendPayRate
    totalPay = weekdayPay + weekendPay
    print("\nPayment Details:")
    print(f"\nWeekday pay amount: {weekdayPay:>11.2f}\nWeekend pay amount: {weekendPay:>11.2f}\nTotal: {totalPay:>24.2f}")



if __name__ == '__main__':
    get_worker_values()