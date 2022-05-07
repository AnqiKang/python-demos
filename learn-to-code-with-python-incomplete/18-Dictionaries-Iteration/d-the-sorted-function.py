# sort(): sort a variety of iterable inputs. including strings, lists, dicts and more.
# it will not change the original object
numbers = [4, 7, 2, 9]
print(sorted(numbers))
print(numbers)

saleries = {
    "Executive Assistant": 20,
    "CEO": 100
}

# sort() in dict will give a list
print(sorted(saleries))

wheel_count = {
    "truck": 2,
    "car": 4,
    "bus": 8
}

print(sorted(wheel_count.items()))
for veh, count in sorted(wheel_count.items()):
    print("The next vehicale is a {veh} and it has {count} wheels.")
