"""
Escape characters: a set of special characters that we can inject into our strings.
Python interpreter treats differently from regular text.
always begin backslash -- \
"""

print("This will \nbegin on a \nnew line")

print("\tOnce upon a time")

print("\"To be or not to be, said Hamlet\"")

print("Let's print a backslash: \\")

file_name = "C:\\news\\travel"
print(file_name)

# raw string : don't interpret. Just treat it as a whole bunch of text together
print(r"C:\news\travel\PA")

# beak up code across multiple lines
some_random_numer = 5
some_obsure_cal = 25
some_additional_statistic_fetched_from_somewhere = 10
final = some_random_numer + \
    some_obsure_cal + \
    some_additional_statistic_fetched_from_somewhere

print(final)

print(some_random_numer,
      some_obsure_cal,
      some_additional_statistic_fetched_from_somewhere)
