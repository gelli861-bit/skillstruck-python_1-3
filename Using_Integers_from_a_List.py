add = [int(n) for n in input("Enter a list of numbers. (Use spaces)").split()]
mult = 1
for x in add:
    mult = mult * x

print(mult)

#Mult must start at 1 for multiplying, cause 1 times anything is the other number. but 0 times anything is 0