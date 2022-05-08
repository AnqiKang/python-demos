# append(): add a single element to the end of a list
countries = ["United States", "Canada", "Australia"]
print(len(countries))

countries.append("China")
print(len(countries))

# append() method itself returns None, so no need to assign when append()
# append() modifies the existing list because of mutable
countries = countries.append("Belgium")
print(countries) # None