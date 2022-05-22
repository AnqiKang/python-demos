# the values should only be modified by instant's methods itself.
# encapsulation: the data should be bundled together with methods that work on that data.
# an objects' data should be hidden and the only way to modify it or to access it,
# should be through instance methods


# community standard:suggest to anybody reading our code that they should not modify and attribute
# _attribute
# technically, nothing changed, just a visual signifier to other developers that tells them they should not manually be setting these attributes 
class SmartPhone():
    def __init__(self):
        self._company = "Apple"
        self._firmware = 10.0

    def get_firmware(self):
        return self._firmware

    def set_firmware(self):
        print("Reaching out to the server for the next version")
        self._firmware + 1


iphone = SmartPhone()
print(iphone._company)
print(iphone._firmware)

print(iphone.set_firmware())

# no encapsulation
# iphone.company = "Samsung"
# iphone.firmware = "Nonsense"
# print(iphone.company)
# print(iphone.firmware)


