"""
annotation : is an additional piece of information about sth. 
Function annotations allow us to add metadate or additional information about the expected type of things.
    such as what is parameter type, what is return value type
    just showing expectation. not actual type checking. like documentation
"""


def word_multiplier(word: str, times: int) -> str:
    return word * times


print(word_multiplier("dog", 5))
