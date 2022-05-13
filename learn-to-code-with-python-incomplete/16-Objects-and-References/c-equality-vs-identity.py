# is : identified checks if 2 names point to the actual same object (memory address)
from turtle import st


students = ["bob", "sally", "Karen"]
athletes = students
nerds = ["bob", "sally", "Karen"]

print(students == athletes)  # True
print(students == nerds)  # True

print(students is athletes)  # True
print(students is nerds)  # False

# Python with immutable types like the int, float, string, boolean
# it doesn't bother creating multiple objects for them in memory.
# there is no need for multiple objects to be created
# because these objects cannot be mutated and there is no risk for multiple names referencing the same object because it can;t be modified.

# ex: 100 variables referencing the same string "Hello"
# if you want to overwrite the value of the 1 variable to hold an uppercase version of the string
# call upper() method on that string, and you will get back a brand new string "HELLO" object
# the other 99 objects still be pointing to the original string "Hello"

# so any references to immutable data types will always reference the same object
a = 1
b = 1
print(a == b)  # True
print(a is b)  # True

