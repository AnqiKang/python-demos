the_simpsons = ["Homer", "Marge", "Bart", "Lisa", "Maggie"]
print(the_simpsons[:: -1])

for character in the_simpsons[:: -1]:
    print(f"{character} has a total of {len(character)} characters.")


# built in reversed() --> <list_reverseiterator object at 0x1056515e0>
# not return a list value, it is list_reverseiterator
print(reversed(the_simpsons))
print(type(reversed(the_simpsons)))

for character in reversed(the_simpsons):
    print(f"{character} has a total of {len(character)} characters.")