# when superclass defines __init__ with arguments
# combing both method in the superclass and method in a subclass
class Animal():
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        return f"{self.name} is enjoying the {food}"


class Dog(Animal):
    def __init__(self, name, breed):
        # self.name = name --> duplication
        # super() give us access to the entire namespace or body of the Animal superclass
        # and on this thing, we can invoke anything we want
        # return the parent class, we can invoke any superclass method on it
        super().__init__(name)
        # reference parent class directly. same effect with super(). normally use super()
        # Animal.__init__(name)
        self.breed = breed


watson = Dog("watson", "Golden Retrive")
print(watson.eat("bone"))
print(watson.name)
print(watson.breed)
