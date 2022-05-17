# decorator : a higher order function that both acceptes a function
# as an input then returns another function as an output function

def be_nice(fn):
    def inner():
        print("Nice to meet you! I'm honored to execute your function for you!")
        fn()
        print("Itn was my pleasure executing your function! Have a nice day!")

    return inner


def complex():
    print("Something complex!")

be_nice(complex)()

# syntax sugar: a syntax makes things easier to read or express in a language
# wrap the logic, whenenevr we execute complex1(), it won;t simple do logic within itself. 
# It will do everything the @be_nice has added to it
@be_nice
def complex1():
    print("Something complex!")

complex1()

