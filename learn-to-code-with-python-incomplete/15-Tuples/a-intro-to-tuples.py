# Tuple : A fixed-length immutable list
# mixed data types
foods = ("Sushi", "Steak", "Guacamole")

print(type(foods))  # <class 'tuple'>

# empty tuple
empty = ()
print(type(empty))

# only one element
mystery = (1)
print(type(mystery))  # <class 'int'>

mystery_tuple1 = 1,
print(type(mystery_tuple1))  # <class 'tuple'>

mystery_tuple2 = (1, )
print(type(mystery_tuple2))  # <class 'tuple'>

# using tuple(), elements should within []
print(type(tuple(["Sushi", "Steak", "Guacamole"]))) # <class 'tuple'>



