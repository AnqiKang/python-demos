# Dictionary: an unordered data structure for declaring relationships between objects
# A mutable data structure consisting of pairs of key and values
# Key: is an object that serves as a unique identifier for a value
# Value: is any Python Object
# keys are unqie, value can be duplicates
# Keys must be immutable types (String, integers, floats, tuples)
# values can be any data type

# Dictionaries vs List
# both are mutable
# Dic: key-value pairs added, removed, modified
# Dic is not ordered. It is used for mappings while a list is used for order
# list is ordered

# empty dict
video_game_options = {}
video_game_options = dict()

ice_cream_preferences = {
    "Karen": "Chocolate",
    "Jingyu": "Vanilla",
    "Matt": "Cookies & Creme",
    "Chris": "Chocolate"
}

print(len(ice_cream_preferences))
print(ice_cream_preferences)
