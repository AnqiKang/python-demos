# modify a function signature to accept any number of keyword arguments
# which is one where we provode the name of the parameter along with its argument whenever we invoke a function

# word is parameter
def length(word):
    return len(word)


print(length("Hello"))

# key word arguments
print(length(word="Hello"))

# if the funcation want to accept any number of keyword parameyers


def collect_keyword_arguments(**kwargs):
    print(type(kwargs))  # dict
    print(kwargs)

    for key, value in kwargs.items():
        print(f"The key is {key} and the value is {value}")


collect_keyword_arguments(a=2, b=3, c=4)


# bundle sequential arguments with *args
def args_and_kwargs(a, b, *args):
    print(type(args))  # tuple
    print(args)


args_and_kwargs(1, 2, 3, 4, 5)


def mix(a, b, *args, **kwargs):
    print(f"The total of your regular arguments a and b is {a + b}")  # 1, 2
    print(f"The total of your args tuple is {sum(args)}")  # 3,4,5,6

    dict_total = 0
    for value in kwargs.values():
        dict_total += value
    print(f"the total of your kwargs dictionary is {dict_total}")  # 8,9,10


mix(1, 2, 3, 4, 5, 6, x=8, y=9, z=10)
