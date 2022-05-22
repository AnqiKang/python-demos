# built -in functions:
# getattr/setattr: get or set the value of an attribute on an object without using dot
# when we don;t know the attribute that we will be writing or readng in advance as it may be provided by the user or passed by another part of program or dynamically created on fly.


stats = {
    "name": "BBQ Chicken",
    "price": 19.99,
    "size": "Extra Large",
    "ingredients": ["Chicken", "Onions", "BBQ Sauce"]
}

# setattr(obj,att, value): create an attribut on an object.  dynamically creating attributes
# 3 parameters
# object
# the name of the attribute that you want to create on the obj as a string
# the value to set for that attribute


class Pizza():
    def __init__(self, stats):
        for key, value in stats.items():
            setattr(self, key, value)

# want stats key-value pairs to serve as attributes and their respective values
# Pizza object has 4 attributes (keys)
bbq = Pizza(stats)
print(bbq.size)
print(bbq.ingredients)

# Get a named attribute from an object; getattr(x, 'y') is equivalent to x.y.
# When a default argument is given, it is returned when the attribute doesn't exist; without it, an exception is raised in that case.
# 3 arguments
# object.
# string to represent the name of the attribute whose value you want to access
# default value to return if the att doesn't exist
for att in ["price", "name", "diameter", "discounted"]:
    print(getattr(bbq, att, "Unknown"))


