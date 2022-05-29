from re import A
import unittest


class IdentityTest(unittest.TestCase):
    def test_identicality(self):
        a = [1, 2, 3]
        b = a
        c = [1, 2, 3]

        # because the value should be same. a and b point to the same object. c just have the same value( equal, but not identicial)
        # self.assertEqual(a, b)
        # self.assertEqual(a, c)

        # is same memory location? 
        self.assertIs(a, b) 
        self.assertIsNot(a, c)
        self.assertIsNot(b, c)


if __name__ == "__main__":
    unittest.main()
