# isinstance(): determining whether a given object is made from a specific class
# issubclass(): determining whether a class is a subclass of another class

print(type({"a": 1}))

# Return whether an object is an instance of a class or of a subclass thereof.
print(isinstance(1, int))  # True
print(isinstance({"a": 1}, dict))
print(isinstance([], list))


# if we pass a superclass as second argument
print(isinstance(1, object))  # True
print(isinstance(max, object))

# any of the tuple return True
print(isinstance([], (list, dict)))


class Person():
    pass


class Superhero(Person):
    pass


arnold = Person()
boris = Superhero()

print(isinstance(boris, Superhero))  # True
print(isinstance(boris, Person))  # True

print(isinstance(arnold, Person))  # True
print(isinstance(arnold, Superhero))  # False

print(issubclass(Superhero, Person))  # True
print(issubclass(Person, Superhero))  # False
print(issubclass(Superhero, object))  # True
print(issubclass(Person, object))  # True
