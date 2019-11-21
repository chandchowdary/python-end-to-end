#!python3
import os
os.system("cls")

def outermainfunction(orderbit):
	print("\nthis is the outer function")
	def permanentemployeefunction():
		print("\nprinting the details of permanent employee")
		id=int(input("\nenter the employeeid:"))
		name=input("\nenter the employeename:")
		designation=input("\nenter the designation of employee:")
		sal=float(input("\nenter the employee salary:"))
		hra=float(input("\nenter the employee hra:"))
		da=float(input("\nenter the employee da:"))
		permanentdetailslist=[id,name,designation,sal,hra,da]
		return permanentdetailslist
	
	def temporaryemployeefunction():
		print("\nprinting the details of temporary employee")
		id=int(input("\nenter the employeeid:"))
		name=input("\nenter the employeename:")
		designation=input("\nenter the designation of employee:")
		sal=float(input("\nenter the employee salary:"))
		temporarydetailslist=[id,name,designation,sal]
		return temporarydetailslist
	
	if orderbit==1:
		permanentdetails=permanentemployeefunction()
		print("\nprinting the list:",'{}'.format(permanentdetails))
	
	if orderbit==2:
		temporarydetails=temporaryemployeefunction()
		print("\nprinting the list:",'{}'.format(temporarydetails))

def apifunction(function,orderbit):
	function(orderbit)

print("\nprinting the main module")
print("\n.........000............")
print("\n1.enter the choice for permanent employee")
print("\n2.enter the choice for temporary employee")
casechoice=int(input("\nenter your choice:"))
if casechoice==1:
	apifunction(outermainfunction,casechoice)
if casechoice==2:
	apifunction(outermainfunction,casechoice)
else:
	print("\nenter for the program termination")