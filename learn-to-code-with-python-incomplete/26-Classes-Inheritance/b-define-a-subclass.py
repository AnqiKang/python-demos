# superclass
class Store():
    def __init__(self):
        self.owner = "Karen"

    def exclain(self):
        return "Lots of stuff to by, come inside!"

# subclass, a specific type of superclass
# passing the actual class itself as a reference. 
# This tells Python that we are going to create a new CoffeeShop object 
# thats is going to inherit all the functionality,(attributes, methods) from the Store class
class CoffeeShop(Store):
    pass

starbucks = CoffeeShop()
print(starbucks.owner) # Karen
print(starbucks.exclain()) # Lots of stuff to by, come inside!