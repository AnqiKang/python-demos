"""
default arguments: fallback arguments that are passed to a function if an explicit value is not provided for a parameter
"""

# default arguments: if a and b are not provided in the invocation, what do we want their value to be.
def add(a = 0, b = 0):
    return a + b

print(add(7,8))
print(add(10))
print(add())


def string_adder(a = "", b = " "):
    return a + " " + b

print(string_adder("hello","world"))
