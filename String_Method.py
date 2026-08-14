String = "This Variable is only in uppercase."
Rope = "This Variable is only in lowecase."
Wire = "This Variable is a rope."

print(String.upper())
print(" ")
print(Rope.lower())
print(" ")
print(Wire.replace("rope", "String"))
print(" ")

Strip = " This should be the start, and this should be the end. "
Index = "The first letter is Zero, and each letter past is another letter, spaces and special included."
Slicing = "Want to see what happens when you use the index and cut off words from the sentence."
Reverse = ".sdrawkcab si gnirts sihT"
Split = "See what happens with the .split method!"
Length = "How long is this string?"
Search = "Where is the letter your looking for?"
#You can also Search from the end to start.

print(Strip.strip())
print(" ")
print(Index[0])
print(" ")
print(Index[1])
print(" ")
print(Index[-1])
print(" ")
print(Slicing[8:65])
print(" ")
inverse = Reverse[len(Reverse)::-1]
print(inverse)
print(" ")
print(Split.split())
print(" ")
print(len(Length))
print(" ")
print(Search.find("i"))
print(" ")
print(Search.rfind("i"))
