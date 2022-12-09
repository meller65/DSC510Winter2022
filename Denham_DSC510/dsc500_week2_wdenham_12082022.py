# DSC 510
# Week 2
# Programming Assignment Week 2
# Wes Denham
# 12/8/2022

# Change#:1
# Change(s) Made: Added formatting for currency and numeric values
# Date of Change: 12/8/2022
# Author: Wes Denham
# Change Approved by: Wes Denham
# Date Moved to Production: 12/8/2022

print("Welcome to the Fiber Optic Cable Calculator Program")
name = input("What is the company name? ")
print("Thank you " + name)
# this variable will store the cable feet in decimal format
length = float(input("Enter the length of cable (ft): "))
cable = length * 0.87  # calculation for amount of cable in feet
length_fmt = "{:,}".format(length)  # formatting added for numeric value
cable_fmt = "{:,}".format(cable)  # formatting added for currency calculation
# this will output the cost for fiber optic cable
print("The total price is $", cable_fmt)

f = open("receipt.txt", "w")
f.write(
    "Receipt" +
    "\n" +
    "Customer: " +
    name +
    "\n" +
    "Product Purchased: Fiber Optic Cable" +
    "\n" +
    "Price per ft = $0.87" +
    "\n"
    "Total: " +
    length_fmt +
    "ft" +
    " * $0.87 = $" +
    cable_fmt +
    "\n" +
    "Thank you for your purchase!")
f.close()
print("Receipt Printed to Text File")
