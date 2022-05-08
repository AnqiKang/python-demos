#remove(object): Remove first occurrence of value.
# only remove the first occurance of element if the list has same value of elements
nintendo_games = ["Zelda", "Mario", "Donkey Kong", "Zelda"]
nintendo_games.remove("Zelda")
print(nintendo_games)


# Raises ValueError if the value is not present.
# nintendo_games.remove("Wario")
if "Wario" in nintendo_games:
    nintendo_games.remove("Wario")

if "Mario" in nintendo_games:
     nintendo_games.remove("Mario")

print(nintendo_games)

