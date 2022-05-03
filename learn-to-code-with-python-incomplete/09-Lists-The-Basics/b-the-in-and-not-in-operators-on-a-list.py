# in / not : check th inclusion and not inclusion
print("fast" in "breakfast")
print("fast" in "dinner")


b_meals = ["breakfast", "lunch", 'dinner']
print("lunch" in b_meals)
print("lunchs" in b_meals)
print("snack" not in b_meals)

test_scores = [99.0, 35.0, 23.5]
print(99 in test_scores)  #true

if 1000 not in test_scores:
    print("That value is not in there")

    