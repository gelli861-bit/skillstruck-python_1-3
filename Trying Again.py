year = int(input("What year do you want to check?"))

if year % 4 == 0:
	if year % 100 == 00:
		if year % 400 == 0:
			print(str(year) + " is a leap year")
		else:
			print(str(year) + " is not a leap year")
	else:
		print(str(year) + " is a leap year")
else:
    print(str(year) + " is not a leap year")

#I skimmed over lesson's / forgot and that made this way harder than it was.