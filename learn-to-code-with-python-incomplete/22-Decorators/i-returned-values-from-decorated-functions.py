def be_nice(fn):
    def inner(*args, **kwargs):
        print("Nice to meet you! I'm honored to execute your function for you!")
        # print(args)
        # print(kwargs)
        res = fn(*args, **kwargs)
        print("Itn was my pleasure executing your function! Have a nice day!")
        return res

    return inner


@be_nice
def complex_sum(a, b):
    return a + b


print(complex_sum(a=3, b=5))
