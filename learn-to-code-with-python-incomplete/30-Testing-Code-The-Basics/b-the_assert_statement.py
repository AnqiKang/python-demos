# assert: a built in keyword, checking sth is working as a condition for doing sth else
# if the assertion condition is true, the entire condition evaluate to the None, and it is not to be assigned or used anywhere

def add(x, y):
    assert isinstance(x, int) and isinstance(y, int), "Both arguments must be integer"
    return x + y


print(add(3, 5))
# print(add(3, "5")) --> AssertionError: Both arguments must be integer


