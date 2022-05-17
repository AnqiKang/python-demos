# closure: a programming pattern in which a scope retains access to an enclosing scope's name
# it retains access to an enclosing scopes names, even if that enclosing scope no longer exists
def outer():
    candy = "Snickers"

    def inner():
        return candy

    return inner


# even outer() is done running. Python still keeping track of candy because candy is being relied upon by this inner fucntion
# which Python knows may be invoked after this the_func = outer()
the_func = outer()

print(the_func())
