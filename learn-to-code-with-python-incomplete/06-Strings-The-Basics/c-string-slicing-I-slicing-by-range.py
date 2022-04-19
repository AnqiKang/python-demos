"""
return an entire section of characters. 
[start_index(inclusive) : end_index(exclusive)] 
"""

address = "1600 West Plum Street, Fort Collins, Co 80521"
print(address[0:3])
print(address[0:4])
print(address[0:17])
print(address[5:17])

# no index error. Just go to the end of the string
print(address[10:100])

# negative index : included a negative number 
print(address[34:-6])
print(address[-8:-6])

print(address[-8:36])


# only one number for index, but ":" must in there
print(address[5:])
print(address[-10:])

print(address[:10])
print(address[:-10])

print(address[:])
