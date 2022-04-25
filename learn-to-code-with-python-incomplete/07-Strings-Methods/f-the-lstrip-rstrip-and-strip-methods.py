empty_space = "    content             "
print("Total length :", len(empty_space))


# remove right / left / both left and right space
print(empty_space.rstrip())
print("After removing right spaces:", len(empty_space.rstrip()))

print(empty_space.lstrip())
print("After removing left spaces:", len(empty_space.lstrip()))

print(empty_space.strip())
print("After removing left and right spaces:", len(empty_space.strip()))

# can have arguments
# these characters do not have to be in any order, 
# It is just going to look for any combiniation of them at the very beginning or end of the string.
# if these charaters exist somewhere in the middle, it won;t count. 
website = "www.py  wedu thon.study.edu"
print(website.lstrip("w"))
print(website.rstrip("eud"))
print(website.strip("wedu."))