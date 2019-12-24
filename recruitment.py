print("Welcome to the special recruitment program, please answer the following questions: ")

skills = ["Drawing", "Dancing", "Singing", "Running", "Sleeping"]

cv = {}
cv["name"] = input("What's your name? ")
cv["age"] = input("How old are you? ")
cv["experience"] = input("How many years of experience do you have? ")

cv["skills"] = []

def print_skills():

	print("\nSkills: ")

	for i in range(0,len(skills)):
		print(str(i+1) + ". %s" % skills[i])

	print()

	skill = input("Please enter the number of the skill you have: ")

	cv["skills"].append(skills[int(skill)-1])

print_skills()
print("\nIt's time to add another skill so..")
print_skills()

if (int(cv["age"]) > 21 and int(cv["experience"]) > 2 and "Sleeping" in cv["skills"]):
    print("\nYou have been accepted, Congrats %s." % cv["name"])
else:
    print("\nSorry, you have been rejected. We hope you find a job that suits you more :'( ")