'''
This module was written by LE
'''

Number = int(input("How many numbers will you see?"))

my_list = []
def fibonacci(num):
    if num <= 1:
        return num
    else:
        return (fibonacci(num-1) + fibonacci(num-2))

for i in range(Number):
    my_list.append(fibonacci(i))
print(my_list)


#########
# Add List of Numbers Challenge
# list_of_nums = [int(n) for n in input("Enter a list of numbers, seperated with a space.").split()]
# def add_list(my_list):
#     ''' 
#         This is a recursive function used to sum a list of numbers
#         input: a list of number data types
#         output:  sum of the list
#         Example:
#         >>>> [2, 2, 2, 2]
#         >>>> 8
#     '''
#     if len(my_list) == 1:
#         return my_list[0]
#     else:
#         return my_list[0] + add_list(my_list[1:])

# print(add_list(list_of_nums))



# number = int(input("Give me a random number: "))

# def factorial(num): 
#     if num <= 1:
#         return 1
#     else:
#         return (num * factorial(num - 1))

# print(factorial(number))