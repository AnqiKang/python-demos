# the build-in reversed() function return a generator object that consists of an iterable elements in reverse order. 
# that approach doesn't mutable the original iterable

# reverse(): reverses the order of elements of a list in place
vitamins= ["A","D","K"]
print(vitamins.reverse())  # None
print(vitamins) # ['K', 'D', 'A']
