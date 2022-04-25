# character casting
from turtle import st


story = "once upon a time"

# capitalize(): first character of the original string capitalized
print(story.capitalize())

# title(): first character of each words of the original string capitalized
print(story.title())

# upper(): all upper case characters
print(story.upper())

# lower(): all lower case characters
print("HELLO".lower())

# swapcase(): all upper case characters become lower case characters.
# And all lower case characters become upper case characters
print("AbCdE".swapcase())

# method chaining :
print("BENHAMIN FRANKLIN".lower().title())

# original string will not changed because of immutable
print(story)

# how overwrite original string with a new string? -- reassign
story = story.title()
print(story)
