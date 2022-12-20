
#DSC 510
#Week 4
#Programming Assignment Week 3
#Gloria Torres
#Created: 12/09/2022

#Change#:1
#Change(s) Made: Added IF Statements (Installation cost per foot - line 37 - 44)
#Date of change:12/17/2022
#Author:Gloria Torres

# Business information
print("Welcome to G&M")
store = ("G&M")
address = ("1775 Stagecoach Ct. Powell, OH 43065")
Phone = ("614-398-7878")
Good_Bye_Message = ("Thank you for your business!")

# Month and year of the transaction
Month = str(12)
Year = str(2022)

# Company's name
Company = input("What is your company's name? ")

# Welcome message
print("Hello " + Company + "'s"  " Associate")

# Calculation
number_of_feet_to_be_installed = input("Please enter the number of feet of fiber optic cable to be installed ")
feet = int(number_of_feet_to_be_installed)

#IF Statements
# Installation cost per foot
if feet < 101:
    installation_cost = .87
elif feet < 250:
    installation_cost = .80
elif feet < 500:
    installation_cost = .70
else:
    installation_cost = .50

#Calculation of subtotal,tax and total
installation = float(installation_cost) * int(feet)
tax = float(.075) * installation

#Total = Tax + installation cost
total = tax + installation
print("Thank You! The fiber optic cable installation cost per foot " "is " + str(installation_cost))
print("Subtotal " + str("$ ") + str(installation))
print("Tax" + str(" 7.5 %"))
print("Total " + str("$ ")+ str(total))

#Receipt
print("*" * 49)
print("*" * 49)
print(f"\t\t\t\t\t{store.title()}")
print(f"\t{address.title()}")
print(f"\t\t\t\t{Phone.title()}")
print("*" * 49)
print("*" * 49)
# Month and Date of the Transaction
print("Date: " + Month + "-" + Year)
# Company
print("Company's name:" + Company)
# Calculate Cost
print("Total number of fiber optic cable to be installed: " + str(feet))
print("Cable installation cost per foot " + str(installation_cost))
print("Subtotal " + str("$ ") + str(installation))
print("Tax" + str(" 7.5 %"))
print("Total " + "$ " + str(total))
print("*" * 49)
print(f"\t\t\t{Good_Bye_Message.title()}")

