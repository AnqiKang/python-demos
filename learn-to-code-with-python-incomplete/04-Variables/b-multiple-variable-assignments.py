"""
Python allows us to assign multiple variables to the same value or the same object.
"""

# a is not permanently tied to the b. 
# when b points to a new object, the a will not change.
a = b = 5
b = 10
print(a)
print(b)

# tuple way to assign multiple values with multiple variables in one line.
a, b = 50, 100
print(a)
print(b)