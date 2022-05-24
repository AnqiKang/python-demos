# __eq__ : define equality between objects. When comparing 2 of custom objects. Python has no clue which att are relevant to equality
# True: 2 objects will be considered equal
# False: 2 objects will be considered unequal

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


bob = Student(90, 90, 90)
moe = Student(100, 90, 80)
joe = Student(40, 45, 50)

print(bob.grade)
print(moe.grade)
print(joe.grade)

print(bob == moe)  # invoke __eq__()
print(bob == joe)
