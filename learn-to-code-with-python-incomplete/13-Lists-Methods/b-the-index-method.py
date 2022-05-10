# list.index(value) : find the first index position of a given value in a list
pizzas = [
    "Mushroom",
    "Pepperoni",
    "Sausage",
    "Barbecue Chicken",
    "Pepperoni",
    "Sausage"
]

print(pizzas.index("Barbecue Chicken"))
print(pizzas.index("Pepperoni"))
print(pizzas.index("Sausage"))
# print(pizzas.index("Olives")) --> ValueError: 'Olives' is not in list
if "Olives" in pizzas:
    print(pizzas.index("Olives"))

# list.index(value, start) : find from start position, start is inclusive. 
print(pizzas.index("Pepperoni", 2))
