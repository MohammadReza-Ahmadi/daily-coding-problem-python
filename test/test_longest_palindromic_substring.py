import unittest
from unittest import TestCase

from src.arrays import longest_palindromic_substring


class TestLongestPalindromicSubstring(unittest.TestCase):
    def test_none(self):
        in_str = None
        expected = 0
        actual = longest_palindromic_substring.get_longest_len(in_str)
        self.assertEquals(expected, actual)

    def test_one(self):
        in_str = 'a'
        expected = 1
        actual = longest_palindromic_substring.get_longest_len(in_str)
        self.assertEquals(expected, actual)

    def test_two_not_same(self):
        in_str = 'ab'
        expected = 1
        actual = longest_palindromic_substring.get_longest_len(in_str)
        self.assertEquals(expected, actual)

    def test_two_same(self):
        in_str = 'aa'
        expected = 2
        actual = longest_palindromic_substring.get_longest_len(in_str)
        self.assertEquals(expected, actual)

    def test_3(self):
        in_str = 'aba'
        expected = 2
        actual = longest_palindromic_substring.get_longest_len(in_str)
        self.assertEquals(expected, actual)


if __name__ == '__main__':
    unittest.main()
