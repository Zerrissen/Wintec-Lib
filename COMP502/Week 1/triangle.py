'''
Author: Nathan Hines
Purpose: To draw a triangle using turtle
'''

from turtle import *

def drawTriangle():
    pu()
    goto(-40, -40)
    pd()
    goto(40, -40)
    left(120)
    fd(80)
    left(120)
    fd(80)
    pu()
    goto(-50, -40)
    exitonclick()

if __name__ == '__main__':
    drawTriangle()