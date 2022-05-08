# Sort the list in ascending order and return None.
# The sort is in-place (i.e. the list itself is modified)
# and stable (i.e. the order of two equal elements is maintained).
temperatures = [40, 28, 52, 66, 35]
temperatures.sort()
print(temperatures)


coffees = ["Latte", "Espresso", "Macchiato", "Frappucino"]
coffees.sort()
print(coffees)


# descending
temperatures.sort(reverse=True)
print(temperatures)

# sorted(): Return a new list containing all items from the iterable in ascending order.
coffees = ["Latte", "Espresso", "Macchiato", "Frappucino"]
print(sorted(coffees)) #['Espresso', 'Frappucino', 'Latte', 'Macchiato']
print(sorted(coffees, reverse=True)) #['Macchiato', 'Latte', 'Frappucino', 'Espresso']
print(coffees) # ['Latte', 'Espresso', 'Macchiato', 'Frappucino']