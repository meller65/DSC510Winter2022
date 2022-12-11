# DSC510
# Week 2
# Programming Assignment Week 2
# 12/10/2022
# To calculate the installation cost of fiber

# This will display a welcome message to the user
print('Welcome user to the Fiber Optic Cost Estimator ')
# This will ask the user for the name of the company
Company_name = input('What is the name of the company ?')
# This ask will ask the user for the amount of feet that needs to be installed
Install = int(input('How many feet of fiber will be installed ?'))
# This sets the price
Price = 0.87
# This will calculate the cost based off of what the user will enter
Cost = Install * Price
# This will round the values 2 decimal places
rounded = round(Cost, 2)
# This prints the receipt which displays the company name
# The receipt will display the number of fiber to be installed
# The receipt will also show the calculated cost and total cost
print('Thank you for your Order', Company_name)
print(Install, "of fiber will be installed")
print('Your calculated cost is:', rounded)
print('The total cost is $', rounded)

