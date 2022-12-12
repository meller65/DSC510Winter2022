"""
Course: DSC 510
Purpose: Demonstrate fundamentals of programming with Python variables and math operations
Week: 2
Assignment:Programming Assignment 2.1
Student: Gloria Torres
Created: 12.09.2022
"""
# Business information
print("Welcome to G&M")
store = ("G&M")
address = ("1775 Stagecoach Ct. Powell, OH 43065")
Phone = ("614-398-7878")
Good_Bye_Message = ("Thank you for your business")

# Instalation cost per foot
installation_cost = 0.87

# Month and year of the transaction
Month = str(12)
Year = str(2022)

# Company's name
Company = input("What is your company's name? ")

# Welcome message
print("Hello " + Company + "'s"  " Associate")

# Calculation
number_of_feet_to_be_installed = input("Please enter the number of feet of fiber optic cable to be installed ")
total_cost = .87 * int(number_of_feet_to_be_installed) # Installation cost times the number of cable feet to be installed
print("Thank you!" + " The cable installation cost per foot is $0.87. " + "The total installation cost would be:")
print(str("$ ") + str(total_cost) +(" + tax"))
Grand_total = str(total_cost)
Total_Tax = (total_cost * (.075))# Tax calculation
Amount = ((Total_Tax) + (total_cost))   # Total cost + Tax
Total_Amount = Amount

#Receipt
print("*" * 49)
print(f"\t\t\t\t\t{store.title()}")
print(f"\t{address.title()}")
print(f"\t\t\t\t{Phone.title()}")
print("*" * 49)
# Month and Date of the Transaction
print("Date: " + Month + "-" + Year)
# Company
print("Company's name:" + Company)
# Calculate Cost
print("Number of fiber optic cable feet to be installed: " + number_of_feet_to_be_installed)
print("Installation cost per foot: .87")
print("Total:" + Grand_total)
print("Tax (7.5%): " + str(Total_Tax))
print ("Total amount including tax: " + " $ "  + str(Total_Amount))
print("*" * 49)
print(f"\t\t\t{Good_Bye_Message.title()}")

