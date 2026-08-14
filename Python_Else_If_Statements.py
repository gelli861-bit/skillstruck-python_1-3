numb1 = int(input("Give me a number: "))
numb2 = int(input("Give me another number: "))
numb3 = int(input("Give me one more number: "))

if numb3 <= numb2 <= numb1:
    print(numb3)
elif numb2 < numb3 and numb2 < numb1:
    print(numb2)
else:
    print(numb1)
 
#Just read this, if it still doesn't make sense, it's the operations from scratch.