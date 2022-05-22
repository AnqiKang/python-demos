class Example():
    data = "Class att"


e1 = Example()
e2 = Example()

print(e1.data) # Class att
print(e2.data) # Class att

e1.data = "instance att"
print(e1.data) # instance att
print(e2.data) # Class att



Example.data = "change class att"
print(e1.data) # instance att
print(e2.data) # change class att


del e1.data
print(e1.data) # change class att