# inheritance problem: diamon shaped inheritance
# potentially ambiguous
class FilmMaker():
    def give_interview(self):
        print("I love making movies!")


class Director(FilmMaker):
    pass


class Screenwriter(FilmMaker):
    def give_interview(self):
        print("I love writing scripts")


class JackOfAllTrades(Director, Screenwriter):
    pass


"""
             Filmmaker
             /      \
       Director   Screenwriter
             \      /
         JackOfAllTrades
"""

jack = JackOfAllTrades()
# Based on DFS, JackOfAllTrades --> director --> Filmmaker --> Screenwriter --> Filmmaker
# but because the Filmmaker occurs multiple times in the method resolution order.
# Python removes all earlier occurenceas of the class. It only keeps the last occurrence of this class
# JackOfAllTrades --> director --> Screenwriter --> Filmmaker
jack.give_interview()  # I love writing scripts
print(JackOfAllTrades.mro())

