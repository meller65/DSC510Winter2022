# DSC 510
# Week 4
# 4.1 Programming Assignment Week 4
# Author Brian Bonertz
# 01/04/2023


print('Hello!')
name = input('Please Type Your Company Name.')
print('Welcome', name)   # Combined this phrase into one line
def calculation(feet, price):
    total = feet * price
    return total
feet = int(input('How many feet of fiber optic cable do you need installed?'))
# Removed the int (feet) and placed that function in row 12
print('You Entered', feet, 'feet')   # combined this phrase into one line and changed from "need" to "Stated"
print('Cost Per Foot of Fiber Optic Cable Is')
if feet > 500:
    costperfoot = float(.50)
elif feet > 250:
    costperfoot = float(.70)
elif feet > 100:
    costperfoot = float(.80)
else:
    costperfoot = float(.87)
print("$", "%.2f"%costperfoot)   # Removed spaced in line 20
# Added format function to convert costperfoot to dollar amount with 2 decimals
total_cost = calculation(feet, costperfoot)   # Removed Int from "feet" as it is already done above
print('Total Cost for', name, 'is', '$', ("%.2f"%total_cost))   # Combined this phrase into one line
# Added format function to convert total cost to dollar amount with 2 decimals
print('Thank you for your business!')
