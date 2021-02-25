from unittest import TestCase

from src.arrays.zalando_find_number_of_fair_indexes_in_two_arrays import find_number_of_fair_indexes


class Test(TestCase):
    def test_find_number_of_fair_indexes_1(self):
        arr1 = [2, -2, -3, 3]
        arr2 = [0, 0, 4, -4]
        f = find_number_of_fair_indexes(arr1, arr2)
        self.assertEquals(1, f)

    def test_find_number_of_fair_indexes_2(self):
        arr1 = [4, -1, 0, 3]
        arr2 = [-2, 5, 0, 3]
        f = find_number_of_fair_indexes(arr1, arr2)
        self.assertEquals(2, f)

    def test_find_number_of_fair_indexes_3(self):
        arr1 = [4, -1, 0, 3]
        arr2 = [-2, 6, 0, 4]
        f = find_number_of_fair_indexes(arr1, arr2)
        self.assertEquals(0, f)

    def test_find_number_of_fair_indexes_4(self):
        arr1 = [1, 4, 2, -2, 5]
        arr2 = [7, -2, -2, 2, 5]
        f = find_number_of_fair_indexes(arr1, arr2)
        self.assertEquals(2, f)
