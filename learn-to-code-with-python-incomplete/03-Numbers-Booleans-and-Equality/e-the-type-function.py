"""
An object is an insatnce of a class.
Class : a blueprint from whihc objects are made.
Instance: An object made from a class.

type(): return the class of argument we pass in. What blueprint that obejct is constructed from.

"""
print(type(3))
print(type(3.0))
print(type("3.0"))

print(type(5) == type(10))
print(type(5) == type(5.0)) # False