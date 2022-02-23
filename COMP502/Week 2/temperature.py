'''
Author: Nathan Hines
Purpose: To convert given measurement from celcius to fahrenheit
'''

def convertCelciusToFahren():
    celcius = float(input("Enter temperature in celcius: "))
    fahrenheit = ((9/5) * celcius + 32)
    print(str(celcius) + " degrees celcius is " + str(fahrenheit) + " degrees fahrenheit.")

if __name__ == '__main__':
    convertCelciusToFahren()