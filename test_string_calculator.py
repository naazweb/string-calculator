# class to test the string_calculator.py
import unittest
from string_calculator import add


class TestStringCalculator(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(add(''), 0)

    def test_single_number(self):
        self.assertEqual(add('1'), 1)


# Run the tests
if __name__ == '__main__':
    unittest.main()
