number = 0.123456789

# Return value.__format__(format_spec)
# format_spec defaults to the empty string. 
# See the Format Specification Mini-Language section of help('FORMATTING') for details.
print(format(number, "f")) # 0.123457
print(type(format(number, "f"))) # <class 'str'>

# how many numbers after dot
print(format(number, ".2f")) # 0.12
print(format(number, ".1f")) # 0.1
print(format(number, ".3f")) # 0.123

print(format(0.5, "f")) #0.500000 
print(format(0.5, "%")) # 50.000000%
print(format(0.5, ".2%")) # 50.00%

print(format(8123456, ",")) # 8,123,456