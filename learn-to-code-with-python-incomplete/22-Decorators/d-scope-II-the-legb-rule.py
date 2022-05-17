# LEGB rule: how Python searches for a name in the program: 
# Local --> Enclosing functions --> Global --> Built-in

def outer():
    x = 10

    def inner():
        x = 5
        return x

    return inner()

print(outer())  # 5