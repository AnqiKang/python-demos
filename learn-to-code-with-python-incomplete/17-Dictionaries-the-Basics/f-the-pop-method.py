years = [1991, 1995, 2000, 2007]

# remove last element --[1991, 1995, 2000]
years.pop()
print(years)

# remove element based on index -- [1991, 2000]
years.pop(1)
print(years)

# in dict, pop(key) -- return key-value pair
release_dates = {
    "Python": 1991,
    "Ruby": 1995,
    "Java": 1995,
    "Go": 2007
}
year = release_dates.pop("Ruby")
print(year) # 1995, just value, no key
print(release_dates)

# pop(key, defaultReturnVal)
c_year = release_dates.pop("C++", "default")
print(c_year)

java_year = release_dates.pop("Java", "default")
print(java_year)

# del()
release_dates_2 = {
    "Python": 1991,
    "Ruby": 1995,
    "Java": 1995,
    "Go": 2007
}
del release_dates_2["Java"]
print(release_dates_2)
