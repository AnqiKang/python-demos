# Return the difference of two or more sets as a new set.
# (i.e. all elements that are in this set but not the others(arguments).)

candy_bars = {"Milky Way", "Snickers", "100 Grand"}
sweet_things = {"Sour Patch Kids", "Reeses Pieces", "Snickers"}

print(candy_bars.difference(sweet_things))  # {'Milky Way', '100 Grand'}
print(candy_bars - sweet_things)

print(sweet_things.difference(candy_bars)) # {'Sour Patch Kids', 'Reeses Pieces'}
print(sweet_things - candy_bars)
