# functions can be nested or housed inside the bodies of other functions
# nested functions allow us to split a function into smaller pieces
# by organizing them internally within the body of another function, we sort of indicate that they are related to each other.

def convert_gallons_to_cups(gallons):
    # inner nested function
    def gallons_to_quarts(gallons):
        print(f"Converting {gallons} gallons to quarts!")
        return gallons * 4

    def quarts_to_pints(quarts):
        print(f"Converting {quarts} quarts to pints!")
        return quarts * 2

    def pints_to_cups(pints):
        print(f"Converting {pints} pints to cups!")
        return pints * 2

    quarts = gallons_to_quarts(gallons)
    pints = quarts_to_pints(quarts)
    cups = pints_to_cups(pints)
    return cups


print(convert_gallons_to_cups(1))
print(convert_gallons_to_cups(3))

# cannot invoke nested function directly
# print(pints_to_cups(3)) --> NameError: name 'pints_to_cups' is not defined
