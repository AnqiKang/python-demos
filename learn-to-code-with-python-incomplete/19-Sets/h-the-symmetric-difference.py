candy_bars = {"Milky Way", "Snickers", "100 Grand"}
sweet_things = {"Sour Patch Kids", "Reeses Pieces", "Snickers"}

# Return the symmetric difference of two sets as a new set.
# (i.e. all elements that are in exactly one of the sets.)
print(candy_bars.symmetric_difference(sweet_things)) #{'Reeses Pieces', 'Sour Patch Kids', '100 Grand', 'Milky Way'}
print(candy_bars ^ sweet_things)

print(sweet_things.symmetric_difference(candy_bars)) #{'Reeses Pieces', 'Sour Patch Kids', '100 Grand', 'Milky Way'}
print(sweet_things ^ candy_bars)
