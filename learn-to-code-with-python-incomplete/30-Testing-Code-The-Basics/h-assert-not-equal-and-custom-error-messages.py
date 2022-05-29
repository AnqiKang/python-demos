import unittest


def copy_and_add_ele(val, ele):
    copy = val[:]
    copy.append(ele)
    return copy


class TestInequality(unittest.TestCase):
    def test_inequality(self):
        self.assertNotEqual(1, 2)
        self.assertNotEqual(True, False)
        self.assertNotEqual("hello", "Hello")
        self.assertNotEqual([1, 2], [2, 1])

    def test_copy_add_and_ele(self):
        values = [1, 2, 3]
        result = copy_and_add_ele(values, 4)

        # pass the last one argument into any assertion statement. the string only shows the error message when the assertion fails
        self.assertEqual(result, [1, 2, 3, 4],
                         "Make sure the copy append another list")

        self.assertNotEqual(values, [
                            1, 2, 3, 4], "The function is mutating the input. Make sure you are creating a copy")


if __name__ == "__main__":
    unittest.main()
