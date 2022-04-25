# Method: a funcation that acts upon a specific object
# different with functaions: methods directly connect to an object


# find(): return the lowest index in the string where a substring is found
# if it doesn't exist, return -1
# second argument: starting index
browser = "Google Chrom"
print(browser.find("C"))
print(browser.find("o"))
print(browser.find("k"))

print("Ch" in browser)

# index(): return the index of the first character in the string. 
# if it doesn't exist, raise error
print(browser.index("C"))
# print(browser.index("k"))