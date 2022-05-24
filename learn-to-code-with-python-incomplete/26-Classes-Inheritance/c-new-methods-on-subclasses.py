# subclass can extend the funcationality of its parent
# it can get access to everything the parent can do,
# it also can add additional attributes and methods


from multiprocessing import Manager


class Employee():
    def do_work(self):
        print("I am working!")


class Manager(Employee):
    def waste_time(self):
        print("Wow, this YouTube video lokks fun!")


class Director(Manager):
    def fire_employee(self):
        print("Your are fired!")


e = Employee()
m = Manager()

e.do_work()

# subclass can invoke methods from its parent and itself
m.do_work()
m.waste_time()

# multi level: inherit all of the funcationality of the superclasses above them, and then extend them
d = Director()
d.do_work()
d.waste_time()
d.fire_employee()
