# The zip object yields n-length tuples, 
# where n is the number of iterables passed as positional arguments to zip(). 
# The i-th element in every tuple comes from the i-th iterable argument to zip(). 
# This continues until the shortest argument is exhausted.
breakfasts = ["Eggs", "Cereal", "Banana"]
lunches = ["Sushi", "Chicken Teriyaki", "Soup"]
dinners = ["Steak", "Meatballs", "Pasta"]

print(zip(breakfasts, lunches, dinners))  # <zip object at 0x104fa8dc0>
print(type(zip(breakfasts, lunches, dinners))) # <class 'zip'>
print(list(zip(breakfasts, lunches, dinners))) # [('Eggs', 'Sushi', 'Steak'), ('Cereal', 'Chicken Teriyaki', 'Meatballs'), ('Banana', 'Soup', 'Pasta')]

for breakfast, lunch, dinner in zip(breakfasts, lunches, dinners):
    print(f"My meal for today was {breakfast} and {lunch} and {dinner}.")