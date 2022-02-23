'''
Author: Nathan Hines
Purpose: To convert given measurement from feet to meters
'''

def convertFeetToMeters():
    feet = float(input("Enter measurement in feet: "))
    meter = feet * 0.305
    print(str(feet) + " feet is " + str(meter) + " meters.")

if __name__ == '__main__':
    convertFeetToMeters()
