class Card():
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __repr__(self):
        return f'Card("{self.rank}","{self.suit}")'


c = Card("Ace", "Spades")
print(c)  # <__main__.Card object at 0x10c8e7a00> default standard output.


# customize the string representation of the object
# __str__ : return a user-friendly string representing the object
print(str(c))

# __repr__: used for a more technical representation of the object. If possible, this method should look like a valid Python expression
# a string that represents the code that you would have to execute
print(repr(c))

# order
# __str__ --> __repr__