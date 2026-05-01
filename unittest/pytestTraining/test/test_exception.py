import unittest

class TestException(unittest.TestCase):
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            result = 10 / 0


if __name__ == "__main__":
    unittest.main()
