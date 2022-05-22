# class att are defined on the class instead of any instance
# store data that doesn;t belong on an instance.
class Counter():
    # class att, it is going to be accessible on the class
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def create_two(cls):
        two_counters = [cls(), cls()]
        print(f"new number of counter objs created!:{cls.count}")
        return two_counters


print(Counter.count)  # 0
c1 = Counter()
print(Counter.count)  # 1

c2,c3 = Counter.create_two()
print(Counter.count)

# class atts are shared among all instances. Instances can access these values
print(c1.count) # 3
print(c2.count) # 3
print(c3.count) # 3