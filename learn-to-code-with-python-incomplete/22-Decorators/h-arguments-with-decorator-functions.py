def be_nice(fn):
    def inner(*args, **kwargs):
        print("Nice to meet you! I'm honored to execute your function for you!")
        # print(args)
        # print(kwargs)
        fn(*args, **kwargs)
        print("Itn was my pleasure executing your function! Have a nice day!")

    return inner


@be_nice
def complex(stakeholder, position):
    print(f"Something complex for our {position} {stakeholder}")


# complex("Karen")
complex("Karen", "CEO")
