# DSC 510
# Week 4
# Programming Assignment Week 3
# Gloria Torres
# Created: 12/09/2022

# Change#:1
# Change(s) Made: Added IF Statements (Installation cost per foot - line 37 - 44)
# Date of change:12/17/2022
# Author:Gloria Torres

# Change#:2
# Change(s) Made: Modify IF Statement program to add a function to do the heavy lifting
# Date of change:01/05/2023
# Author:Gloria Torres
# Change(s): Line 21, 26,28,44,64,66,82 and 84


# Welcome message
def get_company():
    print("Welcome to G&M")
    company = input("What is your company's name?")
    print('Hello' + company + "'s" " associate." + ' Welcome to my function!')


def main():

    get_company()


if __name__ == '__main__':
    main()

store = "G&M"
address = "1775 Stagecoach Ct. Powell, OH 43065"
Phone = "614-398-7878"
Good_Bye_Message = "Thank you for your business!"

# Month and year of the transaction
Month = str("01")
Year = str(2023)


# Calculation
number_of_feet_to_be_installed = input("Please enter the number of feet of fiber optic cable to be installed ")
feet = int(number_of_feet_to_be_installed)


def cost(installation, tax, total):

    if feet <= 100:
        installation_cost = float(.87)
    elif feet <= 250:
        installation_cost = float(.80)
    elif feet <= 500:
        installation_cost = float(.70)
    else:
        installation_cost = float(.50)

# Calculation of subtotal,tax and total

    installation = float(installation_cost) * int(feet)
    tax = float(.075) * installation
# Total = Tax + installation cost
    total = tax + installation
    print("The fiber optic cable installation cost per foot is: $", format(installation_cost, ",.2f"))
    print("Subtotal: $", format(installation, ",.2f"))
    print("Tax" + str(" 7.5 %"))
    print("Total: $", format(total, ",.2f"))


def main():
    cost('installation', 'tax', 'total')


if __name__ == '__main__':
    main()

# Receipt
print("*" * 49)
print("*" * 49)
print(f"\t\t\t\t\t{store.title()}")
print(f"\t{address.title()}")
print(f"\t\t\t\t{Phone.title()}")
print("*" * 49)
print("*" * 49)
# Month and Date of the Transaction
print("Date: " + Month + "-" + Year)

# Calculate Cost


def main():
    cost('installation', 'tax', 'total')


if __name__ == '__main__':
    main()

print("*" * 49)
print(f"\t\t\t {Good_Bye_Message.title()}")
