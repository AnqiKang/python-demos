# doctest: a lightweight test option
# it searches in our doc strings for pieces of text that look like Python expression.
# piece of Python code that are doing sth with function.
def sum_of_list(numbers):
    """Return the sum of all numbers in a list. below are doctest
    >>> sum_of_list([1,2,3])
    6
    >>> sum_of_list([5,8,13])
    26
    """
    total = 0
    for num in numbers:
        total += num

    return num


if __name__ == "__main__":
    import doctest
    doctest.testmod()
