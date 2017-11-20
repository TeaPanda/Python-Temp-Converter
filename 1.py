import sys
import os

while True:
    print("What is the temperature? Please only use numbers")
    x = int(input(""))
    if -99999 < x < 99999:
        break
    else:
        print("Your number is too big or too small, are you even on earth?")



while True:
    print("Type C if it is in Celsius or F if it is in Fahrenheit")
    unit = input("")

    if unit.capitalize() == "C":
        f = x * (9/5) + 32
        print( x ,"ºC is", f , "ºF")
        break
    elif unit.capitalize() == "F":
        c = (x - 32) * (5/9)
        print( x ,"ºF is", c , "ºC")
        break
    else:
        print("Please insert either C or F")

print("")

if unit.capitalize() == "C":
    k = x + 273.15
    print("Btw, your temperature in Kelvins is" , k)
else:
    k = c + 273.15
    print("Btw, your temperature in Kelvins is" , k)
