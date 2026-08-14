choice1 = int(input("What is the first number?"))
choice2 = int(input("What is the second number?"))

def my_function(first, second):
	if first < second:
		print(first)
	else:
		print(second)
		

my_function(choice1, choice2)