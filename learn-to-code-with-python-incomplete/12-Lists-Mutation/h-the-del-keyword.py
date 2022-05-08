soups = ["French Onion", "clam Chowder", "Chicken Noodle", "Miso", "Wounton"]

# del: will not return the element being removed. so we cannot save it 
del soups[1]
print(soups)

del soups[-1]
print(soups)

# can remove multiple elements at one time -- slice
del soups[1: 3]
print(soups)

