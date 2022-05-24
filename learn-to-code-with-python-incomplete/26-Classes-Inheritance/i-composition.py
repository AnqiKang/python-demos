# Composition is used to model HAS a relationship. an oject has another object
# this is a design pattern in which an object delegates responsibilities to another object
# that it stores or nest's internally inside itself.

# the attributes that we assign in __init__ can hold any Python object, including custom objects that we have declared
# If a class has too many responsibilities, we can extract some of those responsibilities to their own separate classes

# Each lawyer has a briefcase
# each briefcase holds one or more paper object.
class Paper():
    def __init__(self, text, case):
        self.text = text
        self.case = case


class Briefcase():
    def __init__(self, price):
        self.price = price
        self.papers = []

    def add_paper(self, paper):
        self.papers.append(paper)

    def view_notes(self):
        return [paper.text for paper in self.papers]


class Lawyer():
    def __init__(self, name, briefcase):
        self.name = name
        self.briefcase = briefcase

    def write_note(self, text, case):
        paper = Paper(text, case)
        self.briefcase.add_paper(paper)

    def view_note(self):
        print(self.briefcase.view_notes())


cheap_bf = Briefcase(19.99)
vinny = Lawyer("Vincent", cheap_bf)
vinny.write_note("My client is innocent!", "AS-sZK1")
vinny.write_note("There is no evidence of crime!", "AS-27K1")
vinny.view_note()