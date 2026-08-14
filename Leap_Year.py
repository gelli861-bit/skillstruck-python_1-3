year = int(input("What year do you want to check?"))

if year % 100 == 00:
    print("This number has two 0's at the end.")
else:
    print("This number doesn't have two 0's at the end.")

print(year % 100)