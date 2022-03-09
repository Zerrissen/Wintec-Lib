'''
Author: Nathan Hines 21523561
Pledge of Honour: I pledge by honour that this program is solely my own work.
Description: Display message of the day depending on user inputs.
'''

def get_user_input():
    while True:
        try:
            dayNumber = int(input("Enter day of the week: "))
            pass
        except ValueError:
            print("\nError: Invalid input. Try again.\n")
            continue
        if dayNumber:
            break
    motd(dayNumber)

def motd(dayNumber):
    messages = ["Unknown day!", "Moody Monday", "Treat-yourself Tuesday", "What is Wednesday?", "This is Thursday!", "Freedom Friday!", "Sad Saturday :(", "Sleepy Sunday"]
    if dayNumber < 1 or dayNumber > 7:
        print(messages[0])
    else:
        print(messages[dayNumber])

if __name__ == '__main__':
    get_user_input()