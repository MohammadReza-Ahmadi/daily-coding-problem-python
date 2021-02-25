from unittest import TestCase

from src.arrays.zalando_find_fair_index_in_two_arrays import find_fair_index


class Test(TestCase):
    def test_find_fair_index_1(self):
        arr1 = [2, -2, -3, 3]
        arr2 = [0, 0, 4, -4]
        f = find_fair_index(arr1, arr2)
        self.assertEquals(2, f)

    def test_find_fair_index_2(self):
        arr1 = [4, -1, 0, 3]
        arr2 = [-2, 5, 0, 3]
        f = find_fair_index(arr1, arr2)
        self.assertEquals(2, f)

    def test_find_fair_index_0(self):
        arr1 = [4, -1, 0, 3]
        arr2 = [-2, 6, 0, 4]
        f = find_fair_index(arr1, arr2)
        self.assertEquals(0, f)
