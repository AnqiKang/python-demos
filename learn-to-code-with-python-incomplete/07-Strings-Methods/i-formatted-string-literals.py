# f-strings
# directly inject variables or expressions into a string

name = "Bobby"
adj = "red"
noun = "alien"

mad_libs = f"{name} laughed at the {adj} {noun}."
print(mad_libs)

mad_libs = F"{name} laughed at the {adj} {noun}."
print(mad_libs)

print(f"2 + 2 = {2+2}")
