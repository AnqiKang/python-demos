# import a modules' names directly into the current files namespace
from a_calculator import creator, add

print(creator)
print(add(4, 5))

# other names cannot use
# print(area(4, 5)) --> NameError: name 'area' is not defined
