import unittest

# assertIsInstance/ assertIsNotInstance: validting an object is either made from or not made from a specific class


class ObjectTypeTest(unittest.TestCase):
    def test_is_instance(self):
        self.assertIsInstance(1, int)
        self.assertIsInstance(8.786, float)
        self.assertIsInstance([], list)
        self.assertIsInstance({"a": 2}, dict)

    def test_not_is_instance(self):
        self.assertNotIsInstance("1", int)


if __name__ == "__main__":
    unittest.main()
