# __methods__: use magic methods to make classes behave similarly to python built-in classes
# Hook: A procedure that intercepts a process at some point in its execution

print(3.3 + 4.4)
print(3.3.__add__(4.4))

print(len([1, 2, 3]))
print([1, 2, 3].__len__())


print("h" in "hello")
print("hellon".__contains__("h"))

print(["a", "b", "c"][2])
print(["a", "b", "c"].__getitem__(2))
