#DSC510 winter 2022
#programming Assignment week 2
#author Tom Ferko
#12/6/2022

#Change#:1
#Change(s) Made: tested they variable types on lines and added reciept
#Date of Change: 12/8/2022
#Author: Tom Ferko
#Change Approved by: NA
#Date Moved to Production: NA

#introduction inputs to get name, company, cable needed
name = input('Welcome, what is your name?\n')
print('welcome ' + name)
company = input('What is the name of your company?\n')
cable = input('how many feet of fiber optic cable do you need?\n')

#set variables for the cable pricing
cable_cost = 0.87
cable_raw = float(cable) * cable_cost #ge the base cost for total cable
cable_total = round(cable_raw, 2) #make the total 2 decimal points

#update 12/8/2022 below
#print(type(cable_total)) #check types for variables to concat reciept
#print(type(cable_raw))

#print reciept for customer
reciept = 'Thank you for your purchase ' + name+ ' here are the purchase details''\n' \
          + company+'\n' \
          + cable + ' x ' + str(cable_cost) +'\n' \
          + '$' + str(cable_total)
print(reciept)


