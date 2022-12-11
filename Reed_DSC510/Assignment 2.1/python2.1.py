#DSC 510
#Week 2
#Programming Assignment Week 2
#Nathan Reed
#12/11/2022
#------------------------------

print('Welcome User') # welcomes the user
companyName = input('Please name the company you work for?') # names the company that they work for
cableLength = input('How many feet of fiber optic cable will be installed?') # finds length of cable wanted
cableCost = 0.87 # makes a variable for the cable cost so I can change it later
totalCost = int(cableLength) * cableCost # calculates total cost
print('') # adds a blank between top section and bottom section

print('Receipt')
print('Company Name:', companyName) # prints company name that is previously typed in
print('Number of feet of cable fiber to be installed:', cableLength + "ft.") # prints cable fiber ft. to be installed
print('Total Cost: $' + str(totalCost)) # says the total cost
