# File: eBay Dropshipping Price Calculator
# Name: Paul Brasfield
# Date: 3/28/2018
# Desc: This program calculates takes the source price of an item (including shipping) and
#       applies a 40% price increase to it to give the selling price for a dropshipping
#       store.
# Usage: The program reads input from the user of the source price and shipping cost. The output
#        is the input multiplied by 40% (1.40).

from time import sleep # Using sleep to set a time buffer between inputs if the user enters something that
                       # isn't an integer to avoid mix up of values


def priceInput():
    while True:
        try:
            sourcePrice = float(input("Enter the price of your item: $"))
            sourceTax = float(input("Enter the tax cost of your item (Enter 0 if none): $"))
            sourceShipping = float(input("Enter the shipping cost of your item (Enter 0 if none): $"))

            if (sourcePrice and sourceShipping < 0.0):
                if (sourcePrice and sourceShipping and sourceTax < 0.0):
                    if (sourcePrice or sourceShipping < 0.0):
                        if (sourcePrice or sourceShipping or sourceTax < 0.0):
                            if (sourcePrice and sourceShipping or sourceTax < 0.0):
                                print("Your price cannot be negative\n")
                                sleep(1)
                                continue
        except ValueError:
            print("Your price must be numerical\n")
            sleep(1)
            continue
        
        else:
            break
                
                
    dsPriceCalculation(sourcePrice, sourceTax, sourceShipping)

def dsPriceCalculation(sourcePrice, sourceTax, sourceShipping):
    dsIncrease = 1.40
    dsTotal = (sourcePrice + sourceTax + sourceShipping) * dsIncrease

    print("Your selling price is ${:,.2f}".format(dsTotal))
    endInput = input("\nEnter F to close the program. Press ENTER to calculate another price.\n")

    if(endInput == ""):
        print("---------------------------")
        main()

    if(endInput.upper()== "F"):
        exit

def main():
    priceInput()

main()
