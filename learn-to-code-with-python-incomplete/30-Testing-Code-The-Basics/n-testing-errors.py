import unittest

# test a chunk of code raises an error
# assertRaises(errorType, callBackFunction, paras): without this setip, the function will run into the error regularly and crash the test runner


def divide(x, y):
    if y == 0:
        raise ZeroDivisionError
    return x / y


class DivideTestCase(unittest.TestCase):
    def test_divide(self):
        self.assertRaises(ZeroDivisionError, divide, x=10, y=0)

    # with open("fileName.txt", "r") as file:
    # using with-context
    def test_divide_better_way(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)



if __name__ == "__main__":
    unittest.main()
