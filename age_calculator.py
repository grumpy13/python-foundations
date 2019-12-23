from datetime import datetime, date

def check_birthdate(year, month, day):
	birthdate = datetime(year, month, day)
	today = datetime.today().date()
	deltaYear = today.year - birthdate.year
	deltaMonth = 12 - birthdate.month

	if deltaYear >= 0 and deltaMonth >= 0:
		return True
	else:
		return False

def calculate_age(year, month, day):
	birthdate = date(year, month, day)
	today = date.today() 
	age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
	print("You are %s years old." % age)




year = int(input("Enter year of birth: "))
month = int(input("Enter month of birth: "))
day = int(input("Enter day of birth: "))


if check_birthdate(year,month,day):
	calculate_age(year,month,day)
else:
	print("invalid birthdate!")

# print(birthdate.strftime('%Y-%m-%d'))


