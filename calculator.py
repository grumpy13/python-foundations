first = input("Enter the first number: ")

while(not (first.isnumeric())):
	print("invalid number!")
	first = input("Enter the first number: ")


second = input("Enter the second number: ")

while( not (second.isnumeric())):
	print("invalid number!")
	second = input("Enter the second number: ")


operation = input("Choose the operation (+, -, /, *): ")

while((operation != '+') and (operation != '-') and (operation != '/') and (operation != '*')):
	print("operation invalid")
	operation = input("Choose the operation (+, -, /, *): ")

first = int(first)
second = int(second)

if operation == '+':
	result = first + second
elif operation == '-':
	result = first - second
elif operation == '/':
	result = first / second
else:
	result = first * second

print("The answer is " + str(result))