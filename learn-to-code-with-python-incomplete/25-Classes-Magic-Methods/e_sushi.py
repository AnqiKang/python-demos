"""
A modul related to the joy of Sushi/
No fishy code found here!
"""

def fish():
    """
    Determines if fish is a good meal choice
    """
    return True

class Salmon():
    """
    Blueprint for a Salmon Object
    """
    def __init__(self) -> None:
        self.testiness = 10

    def bake(self):
        """
        Bake the fish in an oven.
        """
        self.testiness += 10