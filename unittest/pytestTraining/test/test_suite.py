import unittest

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(10 + 5, 15)

class TestSubtract(unittest.TestCase):
    def test_subtract(self):
        self.assertEqual(10 - 5, 5)

    def suite(self):
        test_suite = unittest.TestSuite()

        test_suite.addTest(unittest.makeSuite(TestAdd))
        test_suite.addTest(unittest.makeSuite(TestSubtract))
        return test_suite

if __name__ == "__main__":
    unittest.main()
