# declare functions that accept any number of positional arguments
def accept_stuff(*args):
    print(type(args))  # <class 'tuple'>
    print(args)  # a tuple contains all arguments


accept_stuff(1, 2, 3)


def my_max(*numbers):
    return max(numbers)


print(my_max(1, 100, 89, 2983, 192))


def my_max(nonsense, more_non_sense, *nums):
    print(nonsense)
    print(more_non_sense)
    return max(nums)


print(my_max("KKKK", 100, 2, 3, 4, 5))  # 5


def my_max(*nums, nonsense):
    print(nonsense)
    return max(nums)


print(my_max(1, 2, 3, 4, 5, nonsense=100))
