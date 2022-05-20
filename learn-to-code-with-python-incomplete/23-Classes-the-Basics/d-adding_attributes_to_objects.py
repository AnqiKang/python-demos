# attribute: a piece of data stored on an object
class Guitar():
    def __init__(self):
        print(f"A new guitar is being created! This object is {self}")


acoustic = Guitar()
electric = Guitar()

# assign attriobutes to an object
acoustic.wood = "Mahogany"
acoustic.strings = 6
acoustic.year = 1990

electric.nickname = "Sound Viking 3000"

# access these attriutes
print(acoustic.wood)
print(electric.nickname)

# using __init__ set attributes to an object