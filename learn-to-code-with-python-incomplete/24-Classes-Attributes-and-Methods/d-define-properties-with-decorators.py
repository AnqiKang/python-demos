# Decorator: A function that accepts a funtion, enhance it, and returns it
# placing built-in decorator before and after getter and setter methods to declare them as properties.
# with this approach, the name of get and set methods can be identical
class Currency():
    def __init__(self, dollars):
        self._cents = dollars * 100

    # this is the getter that will retrieve the value of the property
    @property
    def dollars(self):
        return self._cents / 100

    # setter method
    @dollars.setter
    def dollars(self, dollars):
        if dollars >= 0:
            self._cents = dollars * 100


bank_account = Currency(5000)
print(bank_account.dollars)

bank_account.dollars = 1000
print(bank_account.dollars)
