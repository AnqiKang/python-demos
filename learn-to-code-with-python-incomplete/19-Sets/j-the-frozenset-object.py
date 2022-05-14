# frozenset() -> empty frozenset object frozenset(iterable) -> frozenset object
# Build an immutable unordered collection of unique elements.
mr_freeze = frozenset([1, 2, 3, 2])
print(mr_freeze)  # <class 'frozenset'>
print(type(mr_freeze))

# add, update, remove, discard. any methods that mutates or modifies set object is not present on a frozenset
# mr_freeze.add(4)  --> AttributeError: 'frozenset' object has no attribute 'add'

# but because the frozenset is immutable, so it can act as a dict key
regular_set = {1, 2, 3}
# print({ regular_set: "Some value" }) --> TypeError: unhashable type: 'set'

print({mr_freeze: "Some value"})  # {frozenset({1, 2, 3}): 'Some value'}
