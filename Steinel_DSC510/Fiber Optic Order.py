# DSC 510
# Week 2
# Programming Assignment Week 2
# Author Megan Steinel
# 12/8/2022
print('Welcome to Steinel Fiber Optics')
company_name = input('What is your Companys name?\n ')
print('Thank you. We are excited to assist you', company_name)
ft_of_cable = input('How many feet of cable do you need installed?\n ')
print(ft_of_cable, 'sounds good')
install_cost = .87  # price per foot
total_cost = int(ft_of_cable) * install_cost
print('Let me ring you up a receipt.')
print('Receipt of Purchase')
print(company_name)
print('Feet of Fiber Optic Cable:', ft_of_cable)
print('Total Cost:', total_cost)
