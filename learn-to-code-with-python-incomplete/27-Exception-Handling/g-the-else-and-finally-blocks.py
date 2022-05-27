# else: execute only if the try block execute without error

# x = 10

try:
    print(x + 1)
except NameError:
    print("Some variable is not defined")
else: # this else adds some clarity to the code. keep try short
    print("This will print if there is no error in the try")
finally: # always run. used to finalize sth. 
    print("This will print with or without exception.")
    print("close all connection...")


