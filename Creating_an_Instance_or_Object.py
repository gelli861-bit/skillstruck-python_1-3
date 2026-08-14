class Pet:
   
   def __init__(self, name, kind, age):
         self.name = name
         self.kind = kind
         self.age = age

p1 = Pet("pup", "dog", "5")
p2 = Pet("kit", "cat", "6")
p3 = Pet("chick", "chicken", "8")

print(p1)
print(p2)
print(p3)