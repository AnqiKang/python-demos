# keys(): iterable dict view object -- all keys
# values(): iterable dict view object -- all values

prices = {
    "Bitcoin": 400000,
    "Ethereum": 7000,
    "Litecoin": 10
}

print(prices.keys())
print(type(prices.keys()))

print(prices.values())
print(type(prices.values()))

for currency in prices.keys():
    print(currency, end=" ")

for prince in prices.values():
    print(prince, end=" ")

print()

print("Bitcoin" in prices.keys())
