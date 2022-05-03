# break
def contains(values, target):
    found = False
    for val in values:
        if val == target:
            found = True
            break

    return found


print(contains([1, 2, 3, 4, 5], 3))


# continue
def sum_of_positive_numbers(values):
    total = 0

    for value in values:
        if value <= 0:
            continue

        total += value

    return total


print(sum_of_positive_numbers([1, 2, -3, 4]))
