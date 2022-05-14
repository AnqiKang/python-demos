# set() -> new empty set object set(iterable) -> new set object
# Build an unordered collection of unique elements.

# the only way to create an empty set. Because if {}, it will create an empty Dict
set()

print(set([1, 2, 3, 3]))

print(set((1, 2, 3, 3, 2, 1)))

print(set("Hellohello"))

print(set({"key": "value", "key1": "value"}))  # {'key1', 'key'}


philosophers = ["Plato", "Socrates", "Aristotle",
                "Pythagoras", "Socrates", "Plato"]
# de-duplicate
philosophers_set = set(philosophers)
philosophers = list(philosophers_set)
print(philosophers)
