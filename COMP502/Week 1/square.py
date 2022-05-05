'''
Author: Nathan Hines
Purpose: To draw a square using turtle
'''

from turtle import speed, fd, rt, pu, pd, goto, setpos, exitonclick

def choose():
    while True:
        print("Please choose the square draw method!")
        print("\t1. Easy Mode\n\t2. Challenge Mode")
        try:
           choice = int(input("Enter Choice: "))
        except ValueError:
            print("Error: invalid input. Try again.")
            continue
        if choice == 1:
            easy()
            break
        elif choice == 2:
            challenge()
            break
        else:
            print("Unknown error. Try again.")
            continue

def easy():
    speed(1)
    fd(50)
    rt(90)
    fd(50)
    rt(90)
    fd(50)
    rt(90)
    fd(50)
    exitonclick()

def challenge():
    speed(1)
    pu()
    setpos(25, 25)
    pd()
    goto(-25, 25)
    goto(-25, -25)
    goto(25, -25)
    goto(25, 25)
    exitonclick()


if __name__ == '__main__':
    choose()