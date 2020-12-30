import unittest

from src.arrays import longest_palindromic_substring


class TestLongestPalindromicSubstring(unittest.TestCase):
    def test_none(self):
        in_str = None
        expected = None
        actual = longest_palindromic_substring.get_longest_substring(in_str)
        self.assertEquals(expected, actual)

    def test_one(self):
        in_str = 'a'
        expected = 'a'
        actual = longest_palindromic_substring.get_longest_substring(in_str)
        self.assertEquals(expected, actual)

    def test_two_not_same(self):
        in_str = 'ab'
        expected = None
        actual = longest_palindromic_substring.get_longest_substring(in_str)
        self.assertEquals(expected, actual)

    def test_two_same(self):
        in_str = 'aa'
        expected = 'aa'
        actual = longest_palindromic_substring.get_longest_substring(in_str)
        self.assertEquals(expected, actual)

    def test_aba(self):
        in_str = 'aba'
        expected = 'aba'
        actual = longest_palindromic_substring.get_longest_substring(in_str)
        self.assertEquals(expected, actual)

    def test_racecar(self):
        in_str = 'racecar'
        expected = 'racecar'
        actual = longest_palindromic_substring.get_longest_substring(in_str)
        self.assertEquals(expected, actual)

    def test_bbbbbb(self):
        in_str = 'bbbbbb'
        expected = 'bbbbbb'
        actual = longest_palindromic_substring.get_longest_substring(in_str)
        self.assertEquals(expected, actual)

    def test_babfbcb(self):
        in_str = 'babfbcb'
        expected = 'bcb'
        actual = longest_palindromic_substring.get_longest_substring(in_str)
        self.assertEquals(expected, actual)

    def test_babfbck(self):
        in_str = 'babfbck'
        expected = 'bfb'
        actual = longest_palindromic_substring.get_longest_substring(in_str)
        self.assertEquals(expected, actual)


if __name__ == '__main__':
    unittest.main()
