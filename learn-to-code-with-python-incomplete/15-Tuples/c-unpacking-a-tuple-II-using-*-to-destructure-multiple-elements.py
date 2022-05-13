# using * to unpack one or more elements from a tuple into a list
employee = ("Bob", "Johnson", "Manager", 50)

first_name, last_name, *details = employee
print(first_name)
print(last_name)
print(details)
print(type(details))  # <class 'list'>

*name, position, age = employee
print(name)
print(position)
print(age)

first_name, *details, age = employee
print(first_name)
print(details)
print(age)

first_name, last_name, position, *details = employee
print(details) # still list [50]



