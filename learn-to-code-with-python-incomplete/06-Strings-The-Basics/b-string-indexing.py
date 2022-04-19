"""
each character in a string is assigned a numeric position that represents its place in line.
position : index / offset  --> start from 0.
"""

best_language_ever = "Python"
print(best_language_ever[0])
print(type(best_language_ever[0]))

print(best_language_ever[1])

print(best_language_ever[2 * 2])

# string index out of range
# print(best_language_ever[100])

"""
negative index: the character to extract from the end of the string
start from -1
"""

best_language_ever = "Python"
print(best_language_ever[-1])

