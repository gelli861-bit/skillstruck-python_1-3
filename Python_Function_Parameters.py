month = int(input("Which month?  1-12"))

def invitation (choice) :
	if choice == 4 or choice == 6 or choice == 9 or choice == 11:
		print(30)
	elif choice == 2:
		print(28)
	else:
		print(31) 
	

invitation(month)