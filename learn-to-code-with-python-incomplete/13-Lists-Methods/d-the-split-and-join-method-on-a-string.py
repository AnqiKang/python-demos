# string.split(delimiter, maxsplit): split a string based on the occurrences of a delimiter . return value is a list
# delimiter is a substring within in our original string

users = "Bob, Dave, John, Sue, Randy, Meg"
user_list = users.split(', ')
print(user_list) # ['Bob', 'Dave', 'John', 'Sue', 'Randy', 'Meg']

# maxsplit: Maximum number of splits to do. -1 (the default value) means no limit.
# after the maxsplit number, all other as one split
print(users.split(", ", 2)) #['Bob', 'Dave', 'John, Sue, Randy, Meg']

# how many words?
sentence = "I am learning how to code"
words = sentence.split(" ")
print(len(words))

# "delimeter".join(list): Concatenate any number of strings.
# The string whose method is called is inserted in between each given string. The result is returned as a new string.
address = ["500 Fifth Avenue", "New York", "NY", "10036"]
print(",".join(address)) # 500 Fifth Avenue,New York,NY,10036
print(", ".join(address)) # 500 Fifth Avenue, New York, NY, 10036
print("".join(address)) # 500 Fifth AvenueNew YorkNY10036


print("-".join(["555", "123", "4567"])) # 555-123-4567
print("|".join(["555", "123", "4567"])) # 555|123|4567
print("***".join(["555", "123", "4567"])) # 555***123***4567
