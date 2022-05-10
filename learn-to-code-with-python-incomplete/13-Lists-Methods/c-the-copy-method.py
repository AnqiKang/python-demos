# list.copy(): Return a shallow copy of the list.
# shallow copy: this operation is only effective when you have a simple one dimensional list
# that doesn;t store any nested data structure within it.

units = ["meter", "kilogram", "second", "ampere", "kelvin", "candela", "mole"]
more_units = units.copy()
print(units)
print(more_units)

# stored in different location in memory, modify one will not affect another one.
units.remove("kelvin")
print(units) # ['meter', 'kilogram', 'second', 'ampere', 'candela', 'mole']
print(more_units) # ['meter', 'kilogram', 'second', 'ampere', 'kelvin', 'candela', 'mole']

# shorthand to copy
even_more_units = units[:]
print(even_more_units)

