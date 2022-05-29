import unittest

# None is a special object that is used to represent the absence of a value


def explicit_return_sum(a, b):
    return a + b


def implicti_return_sum(a, b):
    print(a + b)


class TestNone(unittest.TestCase):
    def test_sum_functions(self):
        self.assertIsNone(implicti_return_sum(1, 2))
        self.assertIsNotNone(explicit_return_sum(10, 2))


if __name__ == "__main__":
    unittest.main()
