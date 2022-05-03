# range 前包后不包

# 0 1 2 3 4
for num in range(5):
    print(num, end=" ")
print()

# 3 4 5 6 7 8
for num in range(3, 9):
    print(num, end=" ")
print()

# 10 20 30 40 50 60 70 80 90 100
for num in range(10, 101, 10):
    print(num, end=" ")
print()

# 99 88 77 66 55 44 33 22 11 0
for num in range(99, -1, -11):
    print(num, end=" ")
