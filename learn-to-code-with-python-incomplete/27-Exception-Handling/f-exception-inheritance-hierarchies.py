# one exception can be considered a type of or a more specific example of another exception

# create a base class for exceptions defined by one module
# subclass that class to create specific exception classes for different error conditions

class Mistake(Exception):
    """base class, related to a specific area or domian. such as database error"""
    pass

class StupidMistake(Mistake):
    pass

class SillyMistake(Mistake):
    pass

try:
    raise StupidMistake("Extra stupid mistake")
except Mistake as e:
    print(f"{e}")

try:
    raise SillyMistake("Extra silly mistake")
except Mistake as e:
    print(f"{e}")