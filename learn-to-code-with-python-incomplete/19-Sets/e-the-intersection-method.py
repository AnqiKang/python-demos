candy_bars = {"Milky Way", "Snickers", "100 Grand"}
sweet_things = {"Sour Patch Kids", "Reeses Pieces", "Snickers"}

# Return the intersection of two sets as a new set.
# (i.e. all elements that are in both sets.)
print(candy_bars.intersection(sweet_things))  # {'Snickers'}
print(candy_bars & sweet_things)  # {'Snickers'}


values = {3.0, 4.0, 5.0}
more_values = {3, 4, 5, 6}
print(values.intersection(more_values))  # {3.0, 4.0, 5.0}
print(more_values.intersection(values))  # {3.0, 4.0, 5.0}
print(values & more_values)  # {3.0, 4.0, 5.0}
print(more_values & values)  # {3.0, 4.0, 5.0}
