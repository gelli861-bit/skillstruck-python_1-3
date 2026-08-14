#When Concatenating, it normally uses the "+" symbol, which brings problems when trying to add a Interger to it, mainly because Intigers recognizes that as addition. using ".Format", we can fix that.

string = "The amount of problems we should have is {}"
#The "{}" at the end is important when using ".format", that's where it replaces it with the Integer.
integer = 0

print(string.format(integer))
#This will print "The amount of problems we should have is 0"

#You can also do it with two integers
string2 = "This variable is {} sentences long, but instead of having {} integer, it has twice the amount."
integer2 = 2
integer3 = 1

print(string2.format(integer2, integer3))

#Thats it.