# Global keyword allows us to introduce global scope into a local scope
# the global statement declares that a function will change or create a global variable

x = 10


def change_stuff():
    global x
    x = 15


print(x)
change_stuff()
print(x)  # 15 whenever we reference x in the body of our change_stuff(), we are no longer going to be creating a local variable, but we are going to be treating it as the global variable x
