"""
put a third number after a second colon in the [] that follo a string.
that third number defines the step sequence by which to slice
how many characters we want to jump forward by when moving from one index position to the next
"""

alphabet = "abcdefghijklmnopqrstuvwxyz"
print(alphabet[0:10:2])
print(alphabet[::3])
print(alphabet[4:20:3])
print(alphabet[-20:-8:5])

# reverse order
print(alphabet[::-1])
print(alphabet[::-5])