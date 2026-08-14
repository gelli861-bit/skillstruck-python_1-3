words_count = {}
words = input("Create a list of words").split()
for word in words:
    if word not in words_count:
        words_count[word] = 0
    words_count[word] += 1

biggest = 0
for x in words_count.values():
    if x >= biggest:
        biggest = x

for x, y in words_count.items():
    if y == biggest:
        print(x)