import unittest

import self


class TestList(unittest.TestCase):
    def setUp(self):
        self.my_list = [1, 2, 3]

    def tearDown(self):
        print("Test completed")

    def test_list_length(self):
       self.assertEqual(len(self.my_list), 3)

if __name__ == "__main__":
    unittest.main()