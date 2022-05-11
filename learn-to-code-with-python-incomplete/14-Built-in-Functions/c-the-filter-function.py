animals = ["elephant", "horse", "cat", "giraffe", "cheetah", "dog"]
long_words = [animal for animal in animals if len(animal) > 5]
print(long_words)


def is_long_animal(animal):
    return len(animal) > 5

# filter(function or None, iterable) --> filter object
# Return an iterator yielding those items of iterable for which function(item) is true. 
# If function is None, return the items that are true.
print(list(filter(is_long_animal, animals)))


