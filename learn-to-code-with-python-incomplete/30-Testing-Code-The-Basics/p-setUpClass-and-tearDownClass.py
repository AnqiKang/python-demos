import unittest

# setUpClass / tearDownClass
# run before everything starts up and after everything is done running.
# only do once


class TestOperations(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("This will run ONCE before test suite starts!")

    def setUp(self):
        print("This will run before EACH test!")

    def tearDown(self):
        print("This will run after EACH tests!")

    @classmethod
    def tearDownClass(cls):
        print("This will run ONCE after test suite done!")

    def test_stuff(self):
        self.assertEqual(1, 1)

    def test_more_stuff(self):
        self.assertEqual([], [])


if __name__ == "__main__":
    unittest.main()
