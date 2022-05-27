def divide_five_by_number(n):
    try:
        return 5 / n
    # except ZeroDivisionError:
    #    return "Customize error message: ZeroDivisionError: division by zero"
    # except TypeError as e:
    #  return f"No dividing by invalid objects! {e}"
    except (ZeroDivisionError, TypeError) as e:
        return f"{e}"


print(divide_five_by_number(0))
print(divide_five_by_number(10))
print(divide_five_by_number("Nonsense"))
