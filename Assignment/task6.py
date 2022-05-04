'''PLUS = f"{RESET}[{GOOD}+{RESET}] "cle
Author: Nathan Hines 21523561
Pledge of Honour: I pledge by honour that this program is solely my own work.
Description: Use a loop to draw a pattern of circles
'''

from colorama import init, Fore
from turtle import *

# Constants
ERROR = Fore.RED
INP = Fore.YELLOW
RESET = Fore.RESET
HASH = f"{RESET}[{INP}#{RESET}] "
MINUS = f"{RESET}[{ERROR}-{RESET}] "

# Function to get the number of circles to draw
def get_circle_values():
    # Error catching
    while True:
        try:
            drawingValue = int(input(f"{HASH}Enter an integer between 2-6 (inclusive): {RESET}"))
            pass
        except ValueError:
            print(f"\n{MINUS}{ERROR}Error: Not an integer (whole number). Try again.{RESET}\n")
            continue
        if drawingValue > 6 or drawingValue < 2:
            print(f"\n{MINUS}{ERROR}Error: Value must be between 2-6 (includes integers \'{RESET}2{ERROR}\' and \'{RESET}6{ERROR}\')\n")
            continue
        else:
            break
    draw_image(drawingValue)

# Function to draw the circles and square
def draw_image(drawingValue):
    x, y, rad = 0, 0, 10
    speed(1)

    # Create horizontal circles
    for i in range(drawingValue):
        pu()
        goto(x,y)
        pd()
        fillcolor("blue")
        begin_fill()
        circle(rad)
        end_fill()
        x -= rad * 2

    # Create vertical circles
    for i in range(drawingValue):
        pu()
        goto(x,y)
        pd()
        fillcolor("yellow")
        begin_fill()
        circle(rad)
        end_fill()
        y -= rad * 2

    # Create diagonal circles
    for i in range(drawingValue):
        pu()
        goto(x, y)
        pd()
        fillcolor("red")
        begin_fill()
        circle(rad)
        end_fill()
        x += rad * 2
        y += rad * 2

    # reset coordinates
    x, y = 0, 0
    length = drawingValue * rad * 2
    pu()
    goto(x, y)
    # set to heading with circle
    left(180)
    # create square
    for i in range(4):
        pd()
        fd(length)
        left(90)

# Driver code in case script is run as a module
if __name__ == '__main__':
    init() # loads the colorama module
    get_circle_values()
    exitonclick()