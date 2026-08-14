number = int(input("What number do you want to know?"))

# print(range(1, number))
factors = []
for x in range(2, number):
    if number % x == 0:
        print(x)
    else:
        print(str(number) + " is a prime number")