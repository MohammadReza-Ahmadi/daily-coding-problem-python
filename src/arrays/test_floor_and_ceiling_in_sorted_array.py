import unittest

from src.arrays.floor_and_ceiling_for_given_element_in_sorted_array import get_floor_and_ceiling_of_array_m1_linear_search


class TestFloorAndCeilingInSortedArray(unittest.TestCase):

    def test_7_0(self):
        array = [1, 2, 8, 10, 10, 12, 19]
        x = 0
        expected = [-1, 1]
        actual = get_floor_and_ceiling_of_array_m1_linear_search(array, x)
        self.assertListEqual(actual, expected)

    def test_7_1(self):
        array = [1, 2, 8, 10, 10, 12, 19]
        x = 1
        expected = [1, 1]
        actual = get_floor_and_ceiling_of_array_m1_linear_search(array, x)
        self.assertListEqual(actual, expected)

    def test_7_2(self):
        array = [1, 2, 8, 10, 10, 12, 19]
        x = 2
        expected = [2, 2]
        actual = get_floor_and_ceiling_of_array_m1_linear_search(array, x)
        self.assertListEqual(actual, expected)

    def test_7_2(self):
        array = [1, 2, 8, 10, 10, 12, 19]
        x = 5
        expected = [2, 8]
        actual = get_floor_and_ceiling_of_array_m1_linear_search(array, x)
        self.assertListEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
