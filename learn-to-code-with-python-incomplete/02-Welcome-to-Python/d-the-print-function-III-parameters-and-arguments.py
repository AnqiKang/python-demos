"""
Parameter: a name for an expected argument to a function
Argument: the actual value passed as an input to a function
Sequential Arugument: an argumemnt passed sequentially, in order
Keyword argument: an argument whose parameter name is explicitly written out
Default argumnent: fallback value provided to a parameter if the user does not specify one
"""

print("ABC", "DEF", "XYZ")
print("ABC", "DEF", "XYZ", sep="!")
print("ABC", "DEF", "XYZ", sep="--*--")

print("Hello", end="!&*")
print("Hello")

print("A", "B", "C", sep="**", end="#")
print("A", "B", "C", end="#", sep="**")

