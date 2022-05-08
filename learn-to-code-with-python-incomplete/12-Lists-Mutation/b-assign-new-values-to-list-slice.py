# overwrite multiple list elements  -- slice + assign
coworkers = ["Michael", "Jim", "Dwight", "Pam", "Creed", "Angela"]
coworkers[3:5] = ["Oscar", "Ryan"]
print(coworkers) # ['Michael', 'Jim', 'Dwight', 'Oscar', 'Ryan', 'Angela']

# if slice less than provided values, the list will be expended. -- no error
coworkers[3:5] = ["Oscar", "Ryan", "Meredith"]
print(coworkers) # ['Michael', 'Jim', 'Dwight', 'Oscar', 'Ryan', 'Meredith', 'Angela']

# if slice more than provided values, it will remove some index. -- no error
coworkers[3:5] = ["Oscar"]
print(coworkers) # ['Michael', 'Jim', 'Dwight', 'Oscar', 'Meredith', 'Angela']

# negative slice
coworkers[-3:-1] = ["Ryan"]
print(coworkers)  # ['Michael', 'Jim', 'Dwight', 'Ryan', 'Angela']
