# DSC 510
# Week 2
# Programming Assignment Week 2
# Wes Denham
# 12/8/2022
print("Welcome to the Fiber Optic Cable Calculator Program")
name = input("What is the company name? ")
print("Thank you " + name)
# this variable will store the cable feet in decimal format
length = float(input("Enter the length of cable (ft): "))
cable = length * 0.87  # calculation for amount of cable in feet
# this will output the cost for fiber optic cable
print("The total price is $", round(cable, 2))

f = open("receipt.csv", "w")
f.write(
    "Receipt" +
    "\n" +
    "Customer:" +
    name +
    "\n" +
    "Product Purchased: Fiber Optic Cable" +
    "\n" +
    "Price per ft = $0.87" +
    "\n"
    "Total: " +
    str(length) +
    "ft" +
    " * $0.87 = " +
    str(cable) +
    "\n" +
    "Thank you for your purchase!")
f.close()
print("Receipt Printed")
