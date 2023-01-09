# DSC 510
# Week 4
# 4.1 Programming Assignment Week 4
# Author Brian Bonertz
# 01/04/2023


def main():
    print("Hello!")


if __name__ == "__main__":
    main()


companyname = input('Please Type Your Company Name.')  # changed name to companyname
print('Welcome', companyname)


def calculation(feetofcable, price):    # Added Function
    total = feetofcable * price
    return total


feet = int(input('How many feet of fiber optic cable do you need installed?'))
print('You Entered', feet, 'feet')
print('Cost Per Foot of Fiber Optic Cable Is')
if feet > 500:
    costperfoot = float(.50)
elif feet > 250:
    costperfoot = float(.70)
elif feet > 100:
    costperfoot = float(.80)
else:
    costperfoot = float(.87)

print("$", "%.2f" % costperfoot)

total_cost = calculation(feet, costperfoot)   # called the calculation function
print('Total Cost for', companyname, 'is', '$', ("%.2f" % total_cost))
print('Thank you for your business!')
# removed spaces
