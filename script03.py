#!python3
import os
os.system("cls")
def printuppercase(inparam):
	return inparam.upper()
def printlowercase(inparam):
	return inparam.lower()
def getmessage(infunction):
	message=input("\nenter any message you want to print:")
	printmessage=infunction(message)
	print("\nprinting the message:",'{}'.format(printmessage))

print("\nillustration of higher order functions")
print("\n........000...........................")
print("\n1.print uppercase")
print("\n2.print lowercase")
inchoice=int(input("\nenter your choice:"))
if inchoice==1:
	print("\nprinting the uppercase...")
	getmessage(printuppercase)
elif inchoice==2:
	print("\nprinting the lowercase....")
	getmessage(printlowercase)
else:
	print("\nenter for the exit.....")