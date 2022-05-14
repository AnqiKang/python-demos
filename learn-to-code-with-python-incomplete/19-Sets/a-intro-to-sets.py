# Set: a mutable, unordered data structure that prohibits duplicate values
# we cannot put mutable object like list, dict into a set.
# only immutable objects like numbers, strings, tuples, booleans stc
# no order, no index

stocks = {"MSFT", "FB", "IBM", "FB"}
print(type(stocks))
print(stocks)
print(len(stocks))

prices = {1, 2, 3, 4, 5, 43, 2, 1, 2}
print(prices)

lottery = {(1, 2, 3), (2, 3, 4), (1, 2, 3)}
print(lottery)

print("MSFT" in stocks)

for num in prices:
    print(num, end=" ")

squares = {num ** 2 for num in [-5, 5, -4, 4, -3, 3]}
print(squares) # {16, 25, 9}
