

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# User welcome and user info retrieval along with cost receipt
#DSC 510
#Week 2
#Programming Assignment  2.1
#Author Carlos Cantu
#12/5/2022

print('Hello how are you? I hope you are having a glorious day, welcome!'  )

# retriving the company name
company_name = input('What is your company name?\n')
print ('Thank You \n' + company_name)

# number of feet
optic_cable = float(input('How many feet will you be installing?\n'))
optic_cable_calc = optic_cable *.87
print('Your calculated cost is\n $' + str(f"{optic_cable_calc:,}") )



#receipt
print('****Receipt****')
print('Company Name:\n'+ company_name)
print('Feet To Be Installed:\n' + str(optic_cable))
print('Calculated Cost:\n $' +str(f"{optic_cable_calc:,}") )
print('Total Cost:\n $' + str(f"{optic_cable_calc:,}") )
print('****Thank You****')
