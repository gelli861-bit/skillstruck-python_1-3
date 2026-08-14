#Strings have been a concept from the start. when assigning text to a variable, thats a string.

#Now, normally when you type a long variable, it wraps around the screen when there's no space, but using three quotation marks, it becomes a Multiline string.

WrapAround = "This text is very long, that without any more screen to type on, it wraps around back to the next line, However there isn't a new number, meaning this is defined as the same line. In reality, this string of text is just a really long line."

Multiline = '''This text is also very long.
Now it isn't, because i pressed return and made a new line.
This means that this isn't using the same line of code anymore.
and as long as i press enter, i can go as long as i want.'''

#When printing, the wrap around will still use the same line, meaning some letters of a word may appear on the next line, due to the lack of space, but the multiline will have each line of code seperated by whats one each line of the code.

print(WrapAround)
print(" ")
print(Multiline)