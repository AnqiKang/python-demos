import unittest

# setUp / tearDown
#  Fixture: a piece of code that constructs and configure an onject system under test
# so the tests can focus on the assertions rather than teh setup that is required to get there.


class Address():
    def __init__(self, city, state):
        self.city = city
        self.state = state


class Owner():
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Restaurant():
    def __init__(self, address, owner):
        self.address = address
        self.owner = owner

    @property
    def owner_age(self):
        return self.owner.age

    def summary(self):
        return f"This restaurant is owner by {self.owner.name}, and is located in {self.address.city}."


class TestRestaurant(unittest.TestCase):
    # setUp() and tearDown() will be executed before and after each test
    def setUp(self):
        print("This will run before each test!")
        address = Address("New York", "New York")
        owner = Owner("Jackie", 60)
        self.gold_palace = Restaurant(address, owner)

    def tearDown(self):
        print("This will run after each test!")

    def test_owner_age(self):
        self.assertEqual(self.gold_palace.owner.age, 60)

    def test_summary(self):
        self.assertEqual(
            self.gold_palace.summary(),
            "This restaurant is owner by Jackie, and is located in New York."
            ""
        )


if __name__ == "__main__":
    unittest.main()
