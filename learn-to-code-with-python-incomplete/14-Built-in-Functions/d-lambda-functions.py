# lambda function: an anonymous function (a function without a name)
metals = ["gold", "silver", "platinum", "palladium"]

# lambda(keyword) metal(parameter): len(metal)(return value)
print(list(filter(lambda metal: len(metal) > 5, metals)))
print(list(filter(lambda l: len(l) > 5, metals)))

print(list(filter(lambda word: "p" in word, metals)))

print(list(map(lambda word: word.count('l'), metals)))

print(list(map(lambda word: word.replace('s', '$'), metals)))
