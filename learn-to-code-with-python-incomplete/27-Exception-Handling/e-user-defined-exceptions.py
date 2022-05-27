# reusability: same error can be used in multiple places across the code base 
# add more context on the error being encountered

class NegativeNumbersError(Exception):
    """One or more inputs are negative"""
    pass


def add_pos_numbers(a, b):
    try:
        if a <= 0 or b <= 0:
            raise NegativeNumbersError
    except NegativeNumbersError:
        return "Shame on you, not valid!"


print(add_pos_numbers(-4, 10))