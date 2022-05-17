# nonlocal: only be used inside the body of a nested function, 
# it applies the same effect as global to variable, but it does to variable in the enclosing functions scope
def outer():
    bubble_tea = "Black"

    def inner():
        nonlocal bubble_tea
        bubble_tea = "Taro"

    inner()

    return bubble_tea

print(outer())