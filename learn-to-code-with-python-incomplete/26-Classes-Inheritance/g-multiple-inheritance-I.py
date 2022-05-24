# a class can inherit from multiple super classes 
class FrozenFood():
    def thaw(self, minutes):
        print(f"Thawing for {minutes} minutes!")

    def store(self):
        print("putting in the freezer!")
    
class Dessert():
    def add_weight(self):
        print("Putting on the pounds!")

    def store(self):
        print("putting in the refrigerator!")

# can be described as FrozenFood and Dessert
class IceCream(FrozenFood, Dessert):
    pass

ic = IceCream()
ic.add_weight()
ic.thaw(5)

# both superclasses have store()
# the subclass will invoke the method based on arguments order
ic.store()


# mro() return a type's method resolution order.. class method 
print(IceCream.mro()) # [<class '__main__.IceCream'>, <class '__main__.FrozenFood'>, <class '__main__.Dessert'>, <class 'object'>]

