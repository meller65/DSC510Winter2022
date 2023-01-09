# DSC 510
# Week 4
# Programming Assignment Week 4
# Nathan Reed
# 01/08/2023
# ------------------------------

def computeCost(Price, Length):  # creates a function for the code
    if 0 < Length <= 100:
        Price = 0.87  # if the length of the cable is less than 100 and greater than 0 it will make cable cost .87
    elif 100 < Length <= 250:
        Price = 0.80  # if the length of the cable is less than 250 and greater than 100 it will make cable cost .80
    elif 250 < Length <= 500:
        Price = 0.70  # if the length of the cable is less than 500 and greater than 250 it will make cable cost .70
    elif Length > 500:
        Price = 0.50  # if the length of the cable is greater than 500 it will make cable cost .50
    else:
        print("Please reenter the value. The program will stop now so you can rerun it."), exit()  # makes certain values that don't make sense not possible to happen.
    return Length * Price  # calculates total cost


def main():
    print('Welcome User')  # welcomes the user
    companyName = input('Please name the company you work for?')  # names the company that they work for
    cableLength = input('How many feet of fiber optic cable will be installed?')  # finds length of cable wanted
    cableLength = int(cableLength)  # makes the value an integer, so we can use the operators we want.
    cablePrice = 0  # gives cable price a default value for function above
    totalCost = computeCost(cablePrice, cableLength)
    print('')  # adds a blank between top section and bottom section
    print('Receipt')
    print('Company Name:', companyName)  # prints company name that is previously typed in
    print('Number of feet of cable fiber to be installed:',
          str(cableLength) + "ft.")  # prints cable fiber ft. to be installed
    print('Total Cost: $' + str(totalCost))  # says the total cost


main()
