'''
Author: Nathan Hines 21523561
Pledge of Honour: I pledge by honour that this program is solely my own work.
Description: Draw first letter of family name.
'''
from turtle import pu, setpos, pd, goto, exitonclick


def drawFamilyLetter(): # Function to contain turtle drawing code
    pu()
    setpos(100, 100)
    pd()
    goto(100,-100)
    pu()
    setpos(-100, 100)
    pd()
    goto(-100, -100)
    pu()
    setpos(-100, 10)
    pd()
    goto(100, 10)
    exitonclick()

if __name__ == '__main__': # Driver code if program is used as module
    drawFamilyLetter()