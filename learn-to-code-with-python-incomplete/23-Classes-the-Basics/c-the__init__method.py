# declared in class definition and used to set up instantiation logic for each object created from a class
# __init__ will run automatically whenever an object is instantiated from the class
# __init__: no return value, at least one parameter which represent the object that has been created
class Guitar():
    # self represents the object that is being created that is in the process of being initialized
    def __init__(self):
        print(f"A new guitar is being created! This object is {self}")


# self represents is whatever object is currently in the process of being created
guitar = Guitar() # A new guitar is being created! This object is <__main__.Guitar object at 0x10cd41a00>
print(guitar) # <__main__.Guitar object at 0x108869a00>

