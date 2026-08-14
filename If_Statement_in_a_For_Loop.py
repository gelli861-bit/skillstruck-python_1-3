Lists = [int(n) for n in input("Input a list of numbers").split()]

for x in Lists:
    if x % 2 == 0:
        print(x)
