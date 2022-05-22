# methods are defined and invoked on the class itself
class SushiPlatter():
    def __init__(self, salmon, tuna, shrimp, squid):
        self.salmon = salmon
        self.tuna = tuna
        self.shrimp = shrimp
        self.squid = squid

    # self represnent the instance of the object, class method needn;t
    # cls = class. this method accept the class itself.
    # Python will feed this class to launch_special_A instead of the instance
    @classmethod
    def launch_special_A(cls):
        return cls(salmon=2, tuna=2, shrimp=2, squid=0)

    @classmethod
    def tuna_lover(cls):
        return cls(salmon=0, tuna=10, shrimp=0, squid=0)


karen = SushiPlatter(8, 4, 5, 10)
print(karen.salmon)

lunch_eater = SushiPlatter.launch_special_A()
print(lunch_eater.squid)


tuna_eater = SushiPlatter.tuna_lover()
print(tuna_eater.tuna)


