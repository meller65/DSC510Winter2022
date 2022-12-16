# DSC 510
# Week 3
# 3.1 Programming Assignment Week 3
# Author Brian Bonertz
# 12/16/2022

print('Hello!')
name = input('Please Type Your Company Name.\n')
print('\n')   # Added a space after the user input
print('Welcome', name)   # Combined this phrase into one line
print('\n')
feet = int(input('How many feet of fiber optic cable do you need installed?\n'))
print('\n')   # Added a space after the user input
# Removed the int (feet) and placed that function in row 12
print('You Entered', feet, 'feet')   # combined this phrase into one line and changed from "need" to "Stated"
print('\n')
print('Cost Per Foot of Fiber Optic Cable Is')
costperfoot = float(.87)
print(costperfoot)   # Removed spaced in line 20
total_cost = costperfoot * feet   # Removed Int from "feet" as it is already done above
print('Total Cost for', name, 'is', total_cost)   # Combined this phrase into one line
print('\n')
print('Thank you for your business!')
