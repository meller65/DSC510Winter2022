# purpose of this program: DSC 510 T302
# Assignment number: Week 2
# Name: Fariba Mohammadi

# welcome message
def welcome():
    print("welcome to our shop")


# get company name from the user
def get_com_name():
    comname = input("enter company name: ")
    return comname


# get required fiber len
def get_fiber_len():
    fl = input("How much cable do you need? (feet)")
    return fl


# calculate installation cost
def calc_installation_cost(fiber_len):
    cost = float(fiber_len)*0.87
    return cost


# print the final receipt
def print_receipt():
    welcome()
    print("==================================")
    cname = get_com_name()
    fl = get_fiber_len()
    cost = calc_installation_cost(fl)
    print("==================================")
    print("company name : ", cname)

    print("Fiber len: ", fl)
    print("Total Cost: ", cost)
    print("\n")
    print("==================================")
    print("Thank you for doing business with us")
    print("==================================")


if __name__ == '__main__':
    print_receipt()
