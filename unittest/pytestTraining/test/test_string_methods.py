import unittest

class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual("hello".upper(), "HELLO")

    def test_isupper(self):
        self.assertFalse("hello".isupper())

if __name__ == "__main__":
    unittest.main()
