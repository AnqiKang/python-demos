# multiple objects can react to the same method invocation
# the code should careless about what type an object is and more about what methods it can respond to
# different objects can transder into different things with same method being invoked upon them
class Person():
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def __len__(self):
        return self.height


values = [
    "Karen",
    [1, 2, 3],
    (4, 5, 6, 7),
    {
        "a": 1,
        "b": 2
    },
    Person(name="Karen", height=173)
]

for val in values:
    print(len(val))


# think of behavior instead of object type, the programs are generally going to be more stable
# the behavior of this example is that an object should be able to tell us about its length,
# it is not a specific type, like a string, tuple, dict, Person
# these objects are polymorphic because they are able to respond to the same magic method __len__()
# because of thta, it doesn;t matter what type they are,
# what matters is what messages we can send.