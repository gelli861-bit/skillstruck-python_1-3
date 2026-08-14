my_list = [int(n) for n in input("write a list of numbers").split()]
current = my_list[0]
for x in my_list:
    if x > current:
        print(x)
    current = x
