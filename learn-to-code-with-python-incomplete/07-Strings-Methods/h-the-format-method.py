
# # name, adjective, noun


# # by relative position
# mad_libs = "{} laughed at the {} {}."
# print(mad_libs.format("Bobby", "green", "alien"))
# print(mad_libs.format("Mike", "silly", "tomato"))


# # by number/index position
# mad_libs = "{2} laughed at the {1} {0}."
# print(mad_libs.format("Bobby", "green", "alien"))
# print(mad_libs.format("Mike", "silly", "tomato"))


# # key word
# mad_libs = "{name} laughed at the {adj} {noun}."
# print(mad_libs.format(name="Bobby", adj="green", noun="alien"))
# print(mad_libs.format(adj="green", noun="alien", name="Bobby"))

mad_libs = "{name} laughed at the {adj} {noun}."

name = input("Enter your name: ")
adj = input("Enter an adjective: ")
noun = input("Enter a noun: ")
print(mad_libs.format(name=name, adj=adj, noun=noun))
