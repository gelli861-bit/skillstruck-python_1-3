Sentence = input("Enter a sentence that has more than one use of the letter e.")

#print(

#Needs both instances of E, from start to finish...

#Practice sentence: every word is exactly Destined to use the special Letter from the prompt.

#The result should be 0, and 64

#print(Sentence.find("e"))
#print(Sentence.rfind("e"))

# Now, we need to add them together, in a sentence...
#and they also need to be strings.
print(str(Sentence.find("e")) + "-" + str(Sentence.rfind("e")))
