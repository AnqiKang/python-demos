from mimetypes import init


values = [3, 6, 9, 12, 15, 18, 21, 24]
other_value = [5, 10, 15, 20, 25, 30]


def odd_sum(numbers):
    total = 0
    for num in numbers:
        total = total + num if num % 2 != 0 else total + 0

    return total


def grgreatest_number(numbers):
    max_number = numbers[0]
    for num in numbers:
        max_number = num if num > max_number else max_number

    return max_number


print(odd_sum(values))
print(odd_sum(other_value))


print(grgreatest_number([1, 2, 3]))
print(grgreatest_number([-3, -2, -1]))
