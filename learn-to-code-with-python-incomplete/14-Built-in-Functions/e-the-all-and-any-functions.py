# all(): Return True if bool(x) is True for all values x in the iterable.
# If the iterable is empty, return True.
print(all([True]))
print(all([True, True]))
print(all([True, True, False]))
print(all([1, 2, 3]))
print(all([1, 2, 3, 0]))
print(all(["a", "b"]))
print(all(["a", "b", ""]))
print(all([]))

# Return True if bool(x) is True for any x in the iterable.
# If the iterable is empty, return False.
print(any([True, False]))
print(any([False, False]))
print(any([0, 1]))
print(any([0]))
print(any([" ", ""]))
print(any([""]))
print(any([]))