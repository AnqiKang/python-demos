def reverse(str):
    left = 0
    right = len(str) - 1
    reversed_str = ""
    while left <= right:
        reversed_str += str[right]
        right -= 1

    return reversed_str


print(reverse("straw"))


def reverse_recursion(str):
    if len(str) <= 1:
        return str

    return str[-1] + reverse_recursion(str[0: -1])

print(reverse_recursion("straw"))