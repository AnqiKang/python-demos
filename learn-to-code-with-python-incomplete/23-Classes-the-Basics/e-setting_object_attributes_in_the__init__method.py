# ensure consistency across objects made from the same class
class Guitar():
    def __init__(self, wood):
        self.wood = wood


acoustic = Guitar("Alder")
electric = Guitar("Mahogany")

print(acoustic.wood)
print(electric.wood)

# baritone = Guitar() --> TypeError: __init__() missing 1 required positional argument: 'wood'