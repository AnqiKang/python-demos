"""
positional arguments: based on order
keyword arguments: arguments correspond to a keyword (parameter name)

"""


def add(a, b, c):
    print("The sum of", a, b, "and", b, "is", a + b + c)


add(5, 10, 15)
add(a=5, b=10, c=15)
add(a=5, c=15, b=10)

# begin with positional arguments, then pass in keyword arguments
add(5, c=15, b=10)
add(5, b=10, c=15)
