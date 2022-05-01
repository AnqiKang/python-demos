
def e_positive_or_negative(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    elif number == 0: # ==> else: 
        return "It is Zero!"
     
print(e_positive_or_negative(0))
print(e_positive_or_negative(10))
print(e_positive_or_negative(-10))

def e_calculator(operation, a, b):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b
    else:
        return "Please enter a correct operation!"

print(e_calculator("*", 2, 3))
print(e_calculator("+", 2, 3))
print(e_calculator("/", 2, 3))
print(e_calculator("-", 2, 3))
print(e_calculator("///", 2, 3))

print(abs(-5))