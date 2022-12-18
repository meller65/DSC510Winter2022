#DSC 510
#Week 3
#Programming Assignment Week 3
#Nathan Reed
#12/17/2022
#------------------------------

print('Welcome User') # welcomes the user
companyName = input('Please name the company you work for?') # names the company that they work for
cableLength = input('How many feet of fiber optic cable will be installed?') # finds length of cable wanted
cableLength = int(cableLength) # makes the value an integer so we can use the operators we want.

if cableLength > 0 and cableLength <= 100:
    cableCost = 0.87 # if the length of the cable is less than 100 and greater than 0 it will make cable cost .87
elif cableLength > 100 and cableLength <= 250:
    cableCost = 0.80 # if the length of the cable is less than 250 and greater than 100 it will make cable cost .80
elif cableLength > 250 and cableLength <= 500:
    cableCost = 0.70 # if the length of the cable is less than 500 and greater than 250 it will make cable cost .70
elif cableLength > 500:
    cableCost = 0.50 # if the length of the cable is greater than 500 it will make cable cost .50
else:
    print("Please reenter the value. The program will stop now so you can rerun it."), exit()
# makes certain values that don't make sense not possible to happen.

totalCost = cableLength * cableCost # calculates total cost
print('') # adds a blank between top section and bottom section

print('Receipt')
print('Company Name:', companyName) # prints company name that is previously typed in
print('Number of feet of cable fiber to be installed:', str(cableLength) + "ft.") # prints cable fiber ft. to be installed
print('Total Cost: $' + str(totalCost)) # says the total cost
