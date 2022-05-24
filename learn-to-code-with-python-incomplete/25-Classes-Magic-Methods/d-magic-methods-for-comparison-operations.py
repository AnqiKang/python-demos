# mathematical comparisons and operations between objects
# such as, declare a method that an object is considered greater tahn another student object

# all of these methods logic is arbitrary. How we choose to tell Python to compare, add or subtract,
# it is tottally up to developer
# the importance of defining these methods is these objects are going to play friendly with Puthon built in symbols with built in methods

class Student():
    def __init__(self, math, history, writing):
        self.math = math
        self.history = history
        self.writing = writing

    @property
    def grade(self):
        return self.math + self.history + self.writing

    def __eq__(self, other_student):
        return self.grade == other_student.grade

    # greater than : __gt__()
    def __gt__(self, other_student):
        return self.grade > other_student.grade

     # greater than and equal to: __ge__()
    def __ge__(self, other_student):
        return self.grade >= other_student.grade

    # less than : __lt__()
    def __le__(self, other_student):
        return self.grade < other_student.grade

    # less than and equal to: __le__()
    def __ee__(self, other_student):
        return self.grade <= other_student.grade

    # add +
    def __add__(self, other_student):
        return self.grade + other_student.grade

    # subtract -
    def __asub__(self, other_student):
        return self.grade - other_student.grade


bob = Student(90, 90, 90)  # 270
moe = Student(100, 90, 80)  # 270
joe = Student(40, 45, 50)

print(moe > joe)
print(moe <= joe)
print(moe + joe)