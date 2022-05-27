# exception handling
# code that handles errors, code that runs when a program does not go as planned.
# An exception is an error that occurs during the execution of a program

# Exceptions: a special object that Python uses to manage errors during program execution
# a traceback is a report of the execption that was raised

def divide_five_by_number(n):
    try:
        return  5 / n
    except:
        pass


# print(divide_five_by_number(0)) --> ZeroDivisionError: division by zero
print(divide_five_by_number(0))
print(divide_five_by_number(10))
print(divide_five_by_number("Nonsense"))