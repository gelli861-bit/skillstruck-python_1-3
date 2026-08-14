earningsgoal = int(input("How much money do you want to save in a year?"))
months = earningsgoal / 12
weeks = earningsgoal / 4
days = earningsgoal / 7

print("To save up " + str(earningsgoal) + " dollars in one year, you will need to save " + str(round(months, 2)) + " per month.")
print("To save up " + str(earningsgoal) + " dollars in one year, you will need to save " + str(round(weeks, 2)) + " per week.")
print("To save up " + str(earningsgoal) + " dollars in one year, you will need to save " + str(round(days, 2)) + " per day.")
