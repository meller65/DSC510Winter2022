#DSC 510
#Week 2
#Programming Assignment
#Author Jay Vick
#12/11/2022

#Change 1
#Change to Replace "Hello World" with Welcome Message
#Date of Change 12/11/2022
#Author Jay Vick
#Change Approved by Michael Eller
#Date Moved to Production: 12/11/2022
#Display a welcome message for your user.
WelcomeMessage="Good Day User!"
print(WelcomeMessage)
#Retrieve the company name from the user.
CompanyName=input('Enter Company Name\n')
print (CompanyName)
#Retrieve the number of feet of fiber optic cable to be installed from the user.
FiberCableLength=input('Please enter the number of feet of fiber optic cable to be installed\n')
print (FiberCableLength)
int(FiberCableLength)
#Calculate the installation cost of fiber optic cable by multiplying the total cost as the number of feet times $0.87.
FiberCableCost=int(FiberCableLength)*.87
#Print a receipt for the user including the company name, number of feet of fiber to be installed, the calculated cost, and total cost in a legible format.
from datetime import date
today = date.today()
print("Today's date:", today)
print ('Thank you for Visiting ' +(CompanyName))
print ("Date of Sale", today)
print ('For '+str(FiberCableLength)+' Feet of Fiber Optic Cable your total comes to '+str(FiberCableCost))