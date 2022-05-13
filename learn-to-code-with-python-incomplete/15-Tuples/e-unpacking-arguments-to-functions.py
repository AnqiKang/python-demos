# unpack the values of a list or tuple to serve as sequential arguments to a function
def product(a, b):
    return a * b


print(product(3, 5))

numbers = [3,5]
numbers = (3,5)
# print(product(numbers)) --> TypeError: product() missing 1 required positional argument: 'b'
print(product(*numbers))






