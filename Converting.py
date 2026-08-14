string = "9"
integer = 9
decimal = 9.0
#Just pretend it says float where decimal is.

#All these numbers look the same, but each are different results in code, and don't function the same. However you can convert between each using the first three letter's of what you want to convert it to before a paranthasese "(" *Except for float, just type float before the paranthasese*

converted_string = int(string)
converted_integer = str(integer)
converted_decimal = int(decimal)
decimal_integer = float(integer)

#Converts everything to what you want. 
#When converting a float to integer, it drops the decimal and leaves the number before it, IT DOESN'T ROUND.
