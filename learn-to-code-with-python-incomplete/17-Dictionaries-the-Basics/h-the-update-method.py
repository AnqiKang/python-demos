employ_salarirs = {
    "Guido": 10000,
    "James": 40000,
    "Brandon": 900000
}

extra_employee_salaries = {
    "Yukihiro": 1000000,
    "Guido": 33333
}

# take the parameter, merge it into origin dict. 
# if the key doesn't exist, just add it
# if the key exist, update its value
employ_salarirs.update(extra_employee_salaries)
print(employ_salarirs)
