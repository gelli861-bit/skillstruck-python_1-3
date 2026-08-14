# flowers = [int(n) for n in input("How many blossoms are on each tree?").split()]

# def orchard(flowers):
#     if len(flowers) == 1:
#         pollon = flowers[0] * 3
#         print(pollon)
#     else:
#         mid = len(flowers) // 2
#         first_half = flowers[:mid]
#         second_half = flowers[mid:]
#         orchard(first_half)
#         orchard(second_half)

# orchard(flowers)


# books = [int(n) for n in input("Input an even list of numbers").split()]

# def pairs(books):
#     if len(books) == 2:
#         page = books[0] + books[1]
#         print(page)
#     else:
#         mid = len(books) // 2
#         first_half = books[:mid]
#         second_half = books[mid:]
#         pairs(first_half)
#         pairs(second_half)


# pairs(books)


# this_list = ['panda', 'lion', 'giraffe', 'tiger', 'elephant', 'monkey', 'fish', 'snake', 'bearded dragon', 'koala']

# def feeding(this_list):
#     if len(this_list) == 1:
#         animal = this_list[0]
#         print("The " + animal + " has been fed")
#     else:
#         mid = len(this_list) // 2
#         first_half = this_list[:mid]
#         second_half = this_list[mid:]
#         feeding(first_half)
#         feeding(second_half)

# feeding(this_list)