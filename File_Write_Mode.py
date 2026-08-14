answer = input("What do you want to replace the text with?")

file = open("report.txt", "w")
file.write(answer)
file.close()
file = open("report.txt", "w")
print(file.read())
file.close()