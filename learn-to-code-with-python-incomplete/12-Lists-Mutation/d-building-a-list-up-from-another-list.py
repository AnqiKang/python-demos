# using a beginning list and then applying some operation to each of the elements
# or some of the elements to arrive at a second list

powerball_numbers = [4, 8, 15, 16, 23, 42]


def squares(numbers):
    res = []
    for num in numbers:
        res.append(num ** 2)
    return res


print(squares(powerball_numbers))

def convert_to_floats(numbers):
    res = []
    for num in numbers:
        res.append(float(num))
    return res

print(convert_to_floats(powerball_numbers))

def even_or_odd(numbers):
    res = []
    for num in numbers:
        if num % 2 == 0:
            res.append(True)
        else:
            res.append(False)

    return res

print(even_or_odd(powerball_numbers))