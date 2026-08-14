amount_of_people = int(input("How many people are in the group?"))

numb_large = 0

numb_medium = 0

numb_small = 0

people_left = 0

if amount_of_people % 7 != 0:
    numb_large = int(amount_of_people / 7)
    people_left = amount_of_people % 7
    if people_left % 3 != 0:
        numb_medium = int(people_left / 3)
        numb_small = int(people_left % 3)
    else:
        numb_medium = int(people_left / 3)
else:
    numb_large = int(amount_of_people / 7)




print("You will need " + str(numb_large) + " large pizzas, " + str(numb_medium) + " medium pizzas, and " + str(numb_small) + " small pizzas.")