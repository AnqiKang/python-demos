# Higher Order Function:
# A function that either accepts a function as an argument or returns a function as a return value

def one():
    return 1


print(type(one))  # <class 'function'>


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def calculate(func, a, b):
    return func(a, b)


# pass a funcation as argument
print(calculate(add, 10, 1))  # 11
print(calculate(subtract, 10, 1))  # 9

def invoke_thrice(func):
    func()
    func()

def sample():
    print("A")
    print("B")

invoke_thrice(sample)