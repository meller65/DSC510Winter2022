# DCS 510
# Week 2
# Programming Assignment Week 2
# Author Jocelyn Disla
# 12/08/2022
print('Hello, welcome!')
company = input('What is your company name?\n')  # The user will input their identity that they will be referred to as
# The user will input how many feet they need installed
feet_of_cable = input('How many feet of fiber optic cable do you need installed?\n')
# The users input of how many feet they need installed will be multiplied to the cost of installation
cost_of_install = int(feet_of_cable) * 0.87
# The calculated cost is presented to the user
print('At $0.87 per foot of fiber optic cable, your calculated cost of installation is ${}'.format(cost_of_install))
# Assuring accuracy on the users inputs with the print provided
print('Now {}, if all the presented information is correct, here is your receipt!'.format(company))
# The final receipt is now generated for the user
print(company)
print('Quantity = {}ft of fiber optic cable to be installed'.format(feet_of_cable))
print('Total cost is ${}'.format(cost_of_install))  # This is the total cost that the user will be charged
print('Thank you, please visit us again!')
# Date of change: 12/09/22
# Changes made by Jocelyn Disla
