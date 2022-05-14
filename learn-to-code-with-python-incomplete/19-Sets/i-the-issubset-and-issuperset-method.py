a = {1, 2, 4}
b = {1, 2, 3, 4, 5}

# Report whether another set contains this set.
print(a.issubset(b))  # True
print(a < b)  # True
print(a <= b)  # True
print(b.issubset(a))  # False

# Report whether this set contains another set.
print(b.issuperset(a))  # True
print(b > a)  # True
print(b >= a)  # True
print(a.issuperset(b))  # False
