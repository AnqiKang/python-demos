# scope: a boundary around each piece of data. The locations in a program in whihc a name can be used

# global scope: a variable thta is assigned outside of any function. It just means available within the current file
age = 28
nonsense = 10

# constant: a name fro a value that does not change over the program's execution. (UPPERCASE)
TAX_RATE = 0.06

# local scope: a variable thta is assigned inside of any function. it is limited to sth.
# when the function is done running, the local variable ceases to exist


def fancy_func():
    # shadow variable: a local variable that shares the same name as a global variable
    age = 32
    # if it have local varibale, it will use local variable
    print(age)
    # if no local varibale, it will use global varibale
    print(nonsense)


# print(nonsense) --> "nonsense" is not defined
fancy_func()

# global scope
print(age)


def calculate_tax(price):
    return round(price * TAX_RATE, 2)


def calculate_tip(price):
    return round(price * (TAX_RATE * 3), 2)


print(calculate_tax(10))
print(calculate_tip(10))
