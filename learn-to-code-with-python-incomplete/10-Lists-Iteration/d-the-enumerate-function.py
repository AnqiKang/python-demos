# track the index and value together within a iteration
import enum


errands = {"Go to gym", "Grab lunch", "Get promoted at work", "Sleep"}

# built in function enumerate() --> <enumerate object at 0x10caf3b80>
print(enumerate(errands))

for index, value in enumerate(errands):
    print(f"index = {index}, value = {value}")

# 10 means index start with 10 rather than 0
for index, value in enumerate(errands, 10):
    print(f"index = {index}, value = {value}")