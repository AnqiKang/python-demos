# in / not in
print("erm" in "watermelon")
print("k" in "watermelon")

print(10 in [10, 20, 30])
print(15 in [10, 20, 30])

pokemon = {
    "Fire": ["Charmander", "Charmeleon", "Charizard"],
    "Water": ["Squirtle", "Warturtle", "Blastoies"],
    "Grass": ["Bulbasuar", "Venusaur", "Ivysaur"]
}

# check if key exist
print("Fire" in pokemon)
print("fire" in pokemon)
print("Electric" in pokemon)

print("Electric" not in pokemon)

if "Zombie" in pokemon:
    print(pokemon["Zombie"])
else:
    print("The categry of Zombie does not exist!")
