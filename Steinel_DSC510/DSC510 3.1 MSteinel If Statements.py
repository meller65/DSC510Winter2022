# DSC 510
# Week 3
# Programming Assignment Week 3
# Author Megan Steinel
# 12/16/2022

#Change Control Log:
    #Change#:1
    #Change(s) Made: Added evaluations based on bulk discount for 100+, 250+, and 500+ feet of fiber optic cable.
                     #Added additional comments for increase clarity
    #Date of Change: 12/16/2022
    #Author: Megan Steinel
    #Change Approved by: Megan Steinel
    #Date Moved to Production: 12/16/2022


# Greetings
print('Welcome to Steinel Fiber Optics')
company_name = input('What is your Companys name?\n ')
print('Thank you. We are excited to assist you', company_name)

# Number of feet
amm_of_cable = (input('How many feet of cable do you need installed?\n'))
ft_of_cable = float(amm_of_cable)
print(ft_of_cable, 'Sounds good.\n')

# Bulk discount price/sq foot
if ft_of_cable > 100 and ft_of_cable <= 250:
    install_cost = .80
    print('You will receive an 8% discount for such a large purchase!\n')
elif ft_of_cable > 250 and ft_of_cable <= 500:
    install_cost = .70
    print('You will receive a 19% discount for such a large purchase!\n')
elif ft_of_cable > 500:
    install_cost = .50
    print('You will receive a 42% discount for such a large purchase!\n')
else:
    install_cost = .87
    print('Thank you.\n')

# Total cost
total_cost = int(ft_of_cable) * install_cost

#Customer Receipt
print('Let me ring you up a receipt.\n')

print('Receipt of Purchase')
print('Company Name:', company_name)
print('Feet of Fiber Optic Cable:', ft_of_cable)
print('Total Cost:', total_cost)