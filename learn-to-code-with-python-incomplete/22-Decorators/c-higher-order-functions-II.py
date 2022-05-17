# returining a function from another function

# operation is a string value,
from unittest.util import _count_diff_hashable


def calculator(operation):
    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    if operation == "add":
        return add
    elif operation == "subtract":
        return subtract


print(calculator("add"))  # <function calculator.<locals>.add at 0x10114f160>

# get back a funtion as a return value from calculator, then invoke that function with argument 10, 3
print(calculator("add")(10, 3))  # 13

print(calculator("subtract"))
print(calculator("subtract")(10, 3))


def square(num):
    return num ** 2


def cube(num):
    return num ** 3


def times10(num):
    return num * 10


# store functions into a list
operation = [square, cube, times10]

for func in operation:
    print(func(5))
