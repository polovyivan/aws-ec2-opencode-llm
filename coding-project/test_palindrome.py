import unittest
from palindrome import is_palindrome

class TestPalindrome(unittest.TestCase):
    def test_palindrome(self):
        self.assertTrue(is_palindrome("level"))

    def test_non_palindrome(self):
        self.assertFalse(is_palindrome("hello"))

    def test_mixed_case(self):
        self.assertTrue(is_palindrome("RaceCar"))

    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))

if __name__ == "__main__":
    unittest.main()