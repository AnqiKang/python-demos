# private attributes and private instant's methods don't exist in Python
# Python use protected attributes prefixed with an _ to visuallly indicate that an attribute should be treated as a non-public part of the object API

# name-mangling, Python is going to intentionally twist your mathod names
# and attribute names around, to effectively prevent them from being used buy subclasses

# attributes will be mangled if it begins with a __ double underscore.
# the only time we should use this approcah is when there is the possibility that a subclass will accidentally overwrite sth in your superclass and break the API

class Nonsense():
    def __init__(self):
        self.__some_attribute = "Hello"

    def __some_method(self):
        print("this is coming from some_method!")


class SpecialNonsense(Nonsense):
    pass


n = Nonsense()
sn = SpecialNonsense()

# print(n.__some_attribute) --> AttributeError: 'Nonsense' object has no attribute '__some_attribute'
# print(sn.__some_attribute) --> AttributeError: 'SpecialNonsense' object has no attribute '__some_attribute'
# n.__some_method() --> AttributeError: 'Nonsense' object has no attribute '__some_method'
# sn.__some_method() --> AttributeError: 'SpecialNonsense' object has no attribute '__some_method'

# name mangling 
print(n._Nonsense__some_attribute) # Hello
print(sn._Nonsense__some_attribute) 

n._Nonsense__some_method()
sn._Nonsense__some_method()