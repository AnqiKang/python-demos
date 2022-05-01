# Loop : a series of instructions that is repeated
# count = 0

# while count <= 5:
#     print(f"count = {count}")
#     count += 1

# print(count)


invalid_number = True

while invalid_number:
    user_number = int(input("Enter a number above 10: "))
    if user_number > 10:
        print(f"Thanks, that works! {user_number} is a great choice")
        invalid_number = False
    else:
        print("That dosen't fit! Try again!")

