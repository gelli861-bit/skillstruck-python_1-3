words = input("enter list of words separated by spaces: ").split(" ")
letter_count = []
for x in words:
	if x[0] not in letter_count:
		letter_count.append(x[0])
		letter_count.append(1)
	else:
		letter_count[letter_count.index(x[0])+1] += 1

print(letter_count)

letter = letter_count[0:7:2]
print(letter)
number = letter_count[1:7+1:2]
print(number)

biggest = 0


#The code will read every word in "words", and look at the starting letter, if it already has the letter, it will add 1 to the amount, if not, it will add the letter.
#We want it to only print words that start with the most common letter.
#Judging by how the lesson says i should wait until i had completed the dictionary lessons, and the fact that i had already done this before, i should try to convert it into a dictionary.
#Let's try it: I'm going to seperate the letters from the values, and add them back together as a dictionary
