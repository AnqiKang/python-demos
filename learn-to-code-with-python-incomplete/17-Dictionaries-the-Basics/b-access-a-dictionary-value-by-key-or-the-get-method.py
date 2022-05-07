flight_prices = {
    "Chicago": 199,
    "San Francisco": 499,
    "Denver": 295
}

print(flight_prices["Denver"])


# Key can be any immutable type, can be mixed data type
gym_membership_packages = {
    20: ["Machines"],
    49: ["Machines", "Vitamin Supplement"],
    79: ["Machines", "Vitamin Supplement", "Sauna"]
}

print(gym_membership_packages[49])

# get(key, a defaultValue) ==> map.getOrDefault(key, defaultValue)
print(gym_membership_packages.get(29, ["Basic Dumbbells"]))

# return None, but no key error exception
print(gym_membership_packages.get(100))
