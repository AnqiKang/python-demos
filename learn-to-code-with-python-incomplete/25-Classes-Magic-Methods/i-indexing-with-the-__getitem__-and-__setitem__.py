# __getitem__: define how an object react whenever we try to index into it
# what are we going to extract whenever we provide a pair of [] after our custom objetcs

# __setitem__: 
pillows = {
    "soft": 79.99,
    "hard": 99.19
}

print(pillows["hard"])
print(pillows.__getitem__("soft"))

class CrayonBox():
    def __init__(self):
        self.crayons = []

    def add(self, crayon):
        self.crayons.append(crayon)

    # provide a way for Python to access sth within CrayonBox
    # also establishes an implicit interation protocol for your object. 
    # So we can now iterate over object in a for loop
    def __getitem__(self, index):
        return self.crayons[index]
        
    def __setitem__(self, index, value):
        self.crayons[index] = value


cb = CrayonBox()
cb.add("Blue")
cb.add("Red")

print(cb[0]) # Blue
cb[0] = "Yellow"
print(cb[0]) # Yellow

# because of __getitem__. iteration object
for crayon in cb:
    print(crayon)