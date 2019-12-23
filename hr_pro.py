from datetime import datetime

class Employee:
	def __init__(self,name, age,salary, employement_date):
		self.name=name
		self.age=age
		self.salary=salary
		self.employement_date=employement_date


	def get_working_years(self):
		date = datetime.now()
		today=date.year
		return today - int(self.employement_date)

	def __str__(self):
			return "name: %s age: %s salary: %s working years: %d" % (self.name, self.age, self.salary, self.get_working_years())

class Manager(Employee):
	def __init__(self, name, age, salary, employement_date,bonus_percentage):
		Employee.__init__(self, name, age, salary, employement_date)
		self.bonus_percentage=bonus_percentage

	def get_bonus(self):
		return float(self.bonus_percentage) * float(self.salary)

	def __str__(self):
			return "name: %s age: %s salary: %s working years: %d bonus_percentage: %f" % (self.name, self.age, self.salary, self.get_working_years(), self.get_bonus())


def print_menu():
	print()
	print(" Welcome to HR Pro 2019")
	print("Choose an action to do: ")
	action=[
	"show employees",
	"show managers",
	"add an employee",
	"add a manager",
	"exit",
	]

	action_list=1
	for user_action in action:
		print("  {}. {}".format(action_list, user_action))
		action_list+=1

	choice= int(input("What would you like to do?"))
	print()

	return choice

employees=[]
managers=[]

choice= print_menu()

while choice != 5:
	if(choice==1):
		for e in employees:
			print(e)

	elif (choice==2):
		for m in managers:
			print(m)

	elif (choice==3):
		name = input("Name: ")
		age = int(input("Age: "))
		salary = int(input("Salary: "))
		employement_date = int(input("Employment date: "))

		employee = Employee(name,age,salary,employement_date)
		employees.append(employee)
		print("Employee added succesfully")

	elif (choice==4):
		name = input("Name: ")
		age = input("Age: ")
		salary = input("Salary: ")
		employment_date = input("Employment Year: ")
		bonus_percentage = input("Bonus Percentage: ")
		manager = Manager(name, age, salary, employment_date, bonus_percentage)
		managers.append(manager)
		print("Manager added successfully")
	else:
		print("you have entered an invalid number")

	choice = print_menu()



