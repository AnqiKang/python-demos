import unittest


class InclusionTest(unittest.TestCase):
    # assertIn and assertNotIn: used to check if a value exists or does not exist in an iterable
    def test_inclusion(self):
        # self.assertTrue("k" in "king")
        self.assertIn("k", "king")
        self.assertIn(1, [1, 2, 3])
        self.assertIn(4, (3, 4, 5))
        self.assertIn("a", {"a": 5, "b": 6}.keys())
        self.assertIn(5, {"a": 5, "b": 6}.values())
        self.assertIn(55, range(50, 59))

    def test_non_inclustion(self):
        self.assertNotIn("w", "king")
        self.assertNotIn(10, [1, 2, 3])
        self.assertNotIn(40, (3, 4, 5))
        self.assertNotIn("d", {"a": 5, "b": 6}.keys())
        self.assertNotIn(10, {"a": 5, "b": 6}.values())
        self.assertNotIn(55, range(50, 55))


if __name__ == "__main__":
    unittest.main()
