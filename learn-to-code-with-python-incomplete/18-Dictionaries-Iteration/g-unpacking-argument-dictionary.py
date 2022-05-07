# Dict can be unpacked with **
def height_to_meters(feet, inches):
    total_inches = (feet * 12) + inches
    return total_inches * 0.0254


print(height_to_meters(5, 11))

stats = {
    "feet": 5,
    "inches": 11
}

# unpack dict argument, the keys name and numbers in dict must be same with parameters after unpack
print(height_to_meters(**stats))
