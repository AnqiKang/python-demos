# is used to trigger a specific exception
# we may want to intentionally raise an error so that it can be caught be error handling
# or we may simply not want to program to execute if some prerequisite is not met

def add_positive_numbers(a, b):
    try:
        if a <= 0 or b <= 0:
            raise ValueError(
                "orn or both of the values if invalid. Both numbers must postive!")

        return a + b
    except ValueError as e:
        return f"{e}"

print(add_positive_numbers(10, 5))
# print(add_positive_numbers(10, -5)) --> orn or both of the values if invalid. Both numbers must postive!