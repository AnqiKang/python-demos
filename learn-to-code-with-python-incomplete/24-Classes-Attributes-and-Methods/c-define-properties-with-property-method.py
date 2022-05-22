# getters and setters: instance methods that get/set attribute values on an object
# properties: a mix of an attributes and an instance method
# a property gives the appearance of an attribute on an object. Properties are secretly going to invoke instance methods for us

class Height():
    def __init__(self, feet):
        self._inches = feet * 12

    def _get_feet(self):
        return self._inches / 12

    def _set_feet(self, feet):
        if feet >= 0:
            self._inches = feet * 12
        else:
            self._inches = 0

    # property() accepts 4 arguments, all of which are optional, setter, getter, delete, docString
    # property() give the apperance of attributes, but behind the scenes, it invoke methods for us. 
    feet = property(_get_feet,_set_feet)

h = Height(5)
# feet in there in not an attribute, it is a property
# but whenever we do h.feet, we try to get this value. Python will invoke the very first method that we pass in property() -- _get_feet
print(h.feet) # 5.0

# whenever we try to set a new value on a property, Python will invoke the second method that we pass in propety() -- _set_feet
h.feet = 6
print(h.feet) # 6.0

h.feet = -10
print(h.feet)


