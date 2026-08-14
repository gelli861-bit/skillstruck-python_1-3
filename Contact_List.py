answer = "y"
emptylist = []
while answer == "y":
    name = input("what is the name of your cantact?")
    emptylist.append(name)
    answer = input("do you want to add more contacts? (y or n)")

emptylist.sort()
print(emptylist)