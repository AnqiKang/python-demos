# a comprehensions is a shorthand way to generate an object from another object
# dict, create a dictionary from another iterable object

languages = ["Python", "JavaScripts", "Ruby"]

lengths = {language: len(language)
           for language in languages if "t" in language}
print(lengths)

word = "supercalifragilisticepialidocious"
letter_cnt = {c: word.count(c) for c in word}
print(letter_cnt)
