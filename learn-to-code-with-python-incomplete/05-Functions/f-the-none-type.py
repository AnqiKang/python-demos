"""
None: an empty placeholder, it's NoneType
A function without an explicit rerturn statement will return object None.
"""

a = None
print(type(a))


def subtract(a, b):
    print(a - b)


res = subtract(5, 3)
print(res)  # None
