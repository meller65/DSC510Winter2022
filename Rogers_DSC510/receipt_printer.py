#DSC 510
#Week 2
#Programming Assignment Week 2
#Author Tim Rogers
#12/11/2022

#Welcome message
print("Hello! I am going to print you a receipt!")
#User inputs
Company_name = input("Give me the company name? ")
Cable_length = float(input("How many feet of cable are you buying? "))
#Cost Calculation
Total_cost = .87 * Cable_length
# Here is the Receipt
print(Company_name)
print(Cable_length, "FT")
print("$", "%.2f" % Total_cost)
print("Thank you for your business!")