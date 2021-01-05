import unittest

from src.arrays.find_minimum_diff_between_any_both_element_in_array import find_min_diff


class TestFindMinimumDiffBetweenAnyBothElementInArray(unittest.TestCase):
    def test_6_1(self):
        array = [1, 5, 3, 18, 19, 25]
        expected = 1
        actual = find_min_diff(array)
        self.assertEqual(actual, expected)

    def test_4_4(self):
        array = [30, 5, 20, 9]
        expected = 4
        actual = find_min_diff(array)
        self.assertEqual(actual, expected)

    def test_7_5(self):
        array = [1, 19, -4, 31, 38, 25, 100]
        expected = 5
        actual = find_min_diff(array)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
