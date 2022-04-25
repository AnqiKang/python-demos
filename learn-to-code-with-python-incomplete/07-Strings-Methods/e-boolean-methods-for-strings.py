# these methods relate to the structure or content or casing of a string
print("winter".islower())
print("winter 1234!#%".islower())
print("Winter".islower())


print("SUMMER".isupper())
print("SUMMER 1234!#%".isupper())
print("Summer".isupper())

print("The Four Seasons".istitle())
print("The Four Seasons 1234!#%".istitle())
print("The four Seasons 1234!#%".istitle())

print("Area".isalpha())
print("area".isalpha())
print("area 1234!#%".isalpha())

print("5".isnumeric())
print("5 ".isnumeric())

# either alpha or numeric return True
print("Area51".isalnum())
print("Area 51".isalnum())

print("     ".isspace())
print("  k   ".isspace())