from re import A


# a variable pointing to an immutable object
a = 3
b = a

a = 5
print(a)  # 5
print(b)  # 3

# a variable pointing to an mutable object
a = [1, 2, 3]
b = a  # a and b are pointing to the same object
a.append(4)
print(a)  # [1, 2, 3, 4]
print(b)  # [1, 2, 3, 4]

b.append(5)
print(a)  # [1, 2, 3, 4, 5]
print(b)  # [1, 2, 3, 4, 5]
