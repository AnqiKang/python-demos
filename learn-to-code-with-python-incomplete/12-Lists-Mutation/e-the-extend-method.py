# extend(): add multiple elements to the end of a list.
# Extend list by appending elements from the iterable.
mountains = ["Mount Everest", "K2"]
print(mountains)

mountains.extend(["Kangchenjunga", "Lhotse", "Makalu"])
print(mountains)


extra_mountains = ["Cho Oyu", "Dhaulagiri"]
mountains.extend(extra_mountains)
print(mountains)

# + : return a new list, the original list will not change
steaks = ["Tenderloin", "New York Strop"]
more_steaks = ["T-Bone", "Ribeye"]

my_meal = steaks + more_steaks
print(steaks)
print(more_steaks)
print(my_meal)

# reassign / overwrite
steaks += more_steaks
print(steaks)
