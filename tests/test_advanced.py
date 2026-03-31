import unittest
from advanced_operations import *

class TestAdvanced(unittest.TestCase):

    def test_sqrt(self):
        self.assertEqual(square_root(16), 4)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)

if __name__ == '__main__':
    unittest.main()
