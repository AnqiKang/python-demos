from os import stat


stats = {
    "name": "BBQ Chicken",
    "price": 19.99,
    "size": "Extra Large",
    "ingredients": ["Chicken", "Onions", "BBQ Sauce"]
}


class Pizza():
    def __init__(self, stats):
        for key, value in stats.items():
            setattr(self, key, value)


# hasattr(): check for the existence of an attribute on an object
# 2 arguments
# obj
# string with the name of an attr
# return true or false to indecate the attribute exists on the obj -- safety check before accessing the value of an object att


# delattr():delete an attribute from an object
# 2 argument
# obj
# string with the name of an attr, if the att dosen;t exist, error

bbq = Pizza(stats)
stats_to_delete = ["size", "diameter", "spiciness", 'ingredients']
print(bbq.size)
for stat in stats_to_delete:
    if hasattr(bbq, stat):
        delattr(bbq, stat)


# print(bbq.size) --> AttributeError: 'Pizza' object has no attribute 'size'
