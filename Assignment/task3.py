'''
Author: Nathan Hines 21523561
Pledge of Honour: I pledge by honour that this program is solely my own work.
Description: Display formatted text using user inputs.
'''

def get_worker_values():
    inputPrints = ["Weekday hours worked: ", "Weekend hours worked: ", "Weekday pay rate: "]
    while True:
        for i in inputPrints:
            try: # Checks values of ALL inputs with only one loop! Yay! Increased memory usage but much better UX!
                value = float(input(i))
                pass
            except ValueError:
                print("\nError: Invalid input. Try again.\n")
                continue

            if i == inputPrints[0]:
                weekdaysWorked = value
                continue
                if weekdaysWorked > 120:
                    print("\nError: Too many weekday hours. Try again.\n")
                    continue
            elif i == inputPrints[1]:
                weekendsWorked = value
                continue
                if weekendsWorked > 48:
                    print("\nError: Too many weekend hours. Try again.\n")
                    print("\nError: Values cannot be negative. Try Again.\n")
                    continue
            else:
                break
    calculate_and_display(weekdaysWorked, weekendsWorked, weekdayPayRate, validWeekendPayRate)

def calculate_and_display(weekdaysWorked, weekendsWorked, weekdayPayRate, validWeekendPayRate):
    weekdayPay = weekdaysWorked * weekdayPayRate
    weekendPay = weekendsWorked * validWeekendPayRate
    totalPay = weekdayPay + weekendPay
    print("\nPayment Details:")
    print(f"\nWeekday pay amount: {weekdayPay:>11.2f}\nWeekend pay amount: {weekendPay:>11.2f}\nTotal: {totalPay:>24.2f}")



if __name__ == '__main__':
    get_worker_values()