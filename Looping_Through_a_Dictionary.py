first = int(input("Pick a first number"))
second = int(input("Pick a second number"))			
group = {
	3 : 10,
	5 : 3,
	10 : 6,
	4 : 30,
	first : second
}

total = 0
for x, y in group.items():
	total = total + (x * y)

print(total)