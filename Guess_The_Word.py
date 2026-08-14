mylist = ["python", "the", "world", "luke", "word", "number", "struck", "keyboard", "flower", "bedrock", "system"]

number = int(input("Choose a number between 0 and 10 (0 is an option): "))

word = list(mylist[number])

turns = 12
tries = []

while turns > 0:
    myletter = input("enter a letter that you would like to guess: ")
    if myletter in word:
        print(myletter)
    else:
        print("-")
    turns -= 1

#well, that was more difficult than it needed to be.