# one line syntax to build a new list from an existing iterable object

numbers = [3, 4, 5, 6, 7]


# # normal way
# squares = []
# for number in numbers:
#     squares.append(number ** 2)

# print(squares)

# comperhension
squares = [number ** 2 for number in numbers]
print(squares)


rivers = ["Amazon", "Nile", "Yangtze"]
print([len(river) for river in rivers])

expressions = ["lol", "rofl", "lmao"]
print([expression.upper() for expression in expressions])

# conditionally filter elements during a list comprehension
print(["abcdefghijklmnopqrstuvwxyz".index(char) for char in "donut"])
print([number / 2 for number in range(20)])

donuts = [
    "Boston Cream",
    "Jelly",
    "Vanilla Cream",
    "Glazed",
    "Chocolate Cream"
]

creamy_dounts = [donut for donut in donuts if "Cream" in donut]
print(creamy_dounts)
print([len(donut) for donut in donuts if "Cream" in donut])

print([donut.split(" ")[0] for donut in donuts if "Cream" in donut]) # ['Boston', 'Vanilla', 'Chocolate']

