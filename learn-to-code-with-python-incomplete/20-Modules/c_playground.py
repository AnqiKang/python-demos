# the __name__ special variable which allow us to determin whether a file is being used as a module or as a script
import math
import a_calculator
# import math, a_calculator

print(math.__name__) # math
print(a_calculator.__name__) #a_calculator
print(__name__) # __name__

# if a file is being run as a script, then __name__ will elevate to normal string "__name__"
# if a file is being used as a module, then __name__ will printing in that file will evaluate to the name of the module
print(a_calculator.area(5))