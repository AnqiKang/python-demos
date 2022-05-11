# map(function, iterableObj): invoke the function on every element within iterableObj
numbers = [4, 8, 15, 16, 23, 42]
cubes = [num ** 3 for num in numbers]
print(cubes)


def cube(number):
    return number ** 3


print(map(cube, numbers))  # <map object at 0x10b7193d0>
print(list(map(cube, numbers))) # [64, 512, 3375, 4096, 12167, 74088]

# map(func, *iterables) --> map object
# Make an iterator that computes the function using arguments from each of the iterables. 
# Stops when the shortest iterable is exhausted.
animals = ["cat", "bear", "zebra", "donkey", "cheetah"]
print(list(map(len, animals)))