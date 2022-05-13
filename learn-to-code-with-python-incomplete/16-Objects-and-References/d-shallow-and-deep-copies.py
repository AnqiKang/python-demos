# shallow copy: create a new list and it insert reference into it for all the objects found in the original list.
#               it a great choice if the original list does not contain any nested lists
#                3 ways to create a shallow copy

a = [1, 2, 3]

# 1: slicing
b = a[:]
print(a == b)  # True
print(a is b)  # False

# 2: copy()
c = a.copy()
print(a == c)  # True
print(a is c)  # False

# 3: copy function in the copy module, need to import
import copy
d = copy.copy(a)
print(a == d)  # True
print(a is d)  # False

# shallow copy not a good choice use for nested object
numbers = [2,3,4]
a = [1, numbers, 5]
e = a[:]
print(a == e)  # True
print(a is e)  # False
print(a[1] is e[1]) # True
a[1].append(100)
print(e) # c[1, [2, 3, 4, 100], 5] --> hanging a will affect e


# Deep Copy:  deepcopy() from copy function
f = copy.deepcopy(a)
a.append(1000)
print(a) # [1, [2, 3, 4, 100], 5, 1000]
print(f) # [1, [2, 3, 4, 100], 5]

