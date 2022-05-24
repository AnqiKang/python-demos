# Docstring: a regular Python string that creates technical documentation for a piece of your program
import math
import e_sushi

# module doc
print(e_sushi.__doc__)

# function doc
print(e_sushi.fish.__doc__)

# class doc
print(e_sushi.Salmon.__doc__)

# intance method doc
print(e_sushi.Salmon.bake.__doc__)



print(math.__doc__)

# more formatted,
help(e_sushi)