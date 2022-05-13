# a tuple object can be unpacked, which means we can assign its ordered elements into multiple variables in the program
from re import A


employee = ("Bob", "Johnson", "Manager", 50)

# unpacking
first_name, last_name, position, age = employee
print(first_name, last_name, position, age)


# unpacking also can be used in List
subject, verb, adj = ["Python", "is", "fun"]
print(subject)

# errors
# first_name, last_name, title = employee --> ValueError: too many values to unpack (expected 3)
# first_name, last_name, title, position, age = employee --> ValueError: not enough values to unpack (expected 5, got 4)

a = 5
b = 10

# swap values
b, a = a, b
print(a)  # 10
print(b)  # 5
