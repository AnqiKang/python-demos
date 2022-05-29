import unittest

# tests are written as instance methods inside a class that we are going to define
# TestCase class is a superclass that contains assertions. This class nested within a module called unittest
class TestStringMethods(unittest.TestCase):
    # the methods have to include the word "test" in the title
    def test_split(self):
        pass

if __name__ == "__main__":
    unittest.main()

