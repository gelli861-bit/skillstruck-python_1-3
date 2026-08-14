number = int(input("give me a number: "))

mylist = []
mylist.append(number)

while number != 0:
    number = int(input("give me another number: "))
    mylist.append(number)

add = 0

for x in mylist:
    add = add + x

print(add)