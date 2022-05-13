birthday = (6, 30, 1994)

print(len(birthday))
print(birthday[0])
print(birthday[-1])



# differenct 
# tuple immutable / List mutable
# birthday[1] = 13 --> TypeError: 'tuple' object does not support item assignment

# mutable object itself that within tuple can be changes
addresses = (
    ["Hudson Street", "New York", "NY"],
    ["Franklin Street", "San Francisco", "CA"]
)
addresses[1][0] = ["Something else"]
print(addresses)

print(dir(birthday))


