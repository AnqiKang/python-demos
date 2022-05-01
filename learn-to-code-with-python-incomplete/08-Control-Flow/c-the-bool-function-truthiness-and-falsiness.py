# certain values in Python are truthy, which means they are boolean equivalent is True.
# Other values in Python are falsy which means they are boolean equivalent is False

# Numbers: 
# 0  --> False, other numbers --> True
if -3:
    print("Hello")

if 0:
    print("Will this print?")
 
# String: 
# empty string --> False
if "hello":
    print("La la la")

if "":
    print("Empty string")

if " ":
    print("Just space")

#bool() : Returns True when the argument x is true, False otherwise.
print(bool(1))
print(bool(0))
print(bool(-1.3452))
print(bool(0.0))
