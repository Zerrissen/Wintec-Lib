'''
Author: Nathan Hines
Purpose: To get user input and show possible calulations
'''

def getInput():
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter another number: "))
    calculate(num1, num2)

def calculate(num1, num2):
    numSum = num1 + num2
    numProd = num1 * num2
    numDiv = num1 / num2
    if num1 < num2: # To calculate difference as a positive value
        newnum1 = num2
        newnum2 = num1
        numDiff = newnum1 - newnum2

    print("The following is a display of possible mathematical operations on the two numbers given")
    print("The numbers " + str(num1) + " and " + str(num2) + " were given.")
    print("\tSum: " + str(numSum) +"\n\tDifference: " + str(numDiff) + "\n\tProduct: " + str(numProd) + "\n\tDivison: " + str(numDiv))

if __name__ == '__main__':
    getInput()