'''
Author: Nathan Hines 21523561
Pledge of Honour: I pledge by honour that this program is solely my own work.
Description: Return perimeter and area from given radius of a circle.
'''

import math

def get_radius(): # Function to get the user-given radius
    while True: # Error-catching try-except loop
        try:
            radius = float(input("Please enter the radius of your circle: "))
            pass
        except ValueError:
            print("Error: Invalid input. Try again.")
            continue
        else:
            break
    calculate(radius)

def calculate(radius): # Function to calculate perimeter and area of circle and print
    pi = math.pi
    radsquare = math.pow(radius, 2)
    perimeter = radius * 2 * pi
    area = radsquare * pi
    print("Perimeter: " + str(perimeter) + "\nArea: " + str(area))

if __name__ == '__main__': # Driver code in event of program being used as module
    get_radius()