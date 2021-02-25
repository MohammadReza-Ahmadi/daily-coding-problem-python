from unittest import TestCase

from src.arrays.find_pair_count_of_items_with_sum_of_less_than_a_number import find_count_of_pairs


class Test(TestCase):
    def test_find_count_of_pairs(self):
        arr = [2, 4, 6, 8, 9]
        c = find_count_of_pairs(arr, 14)
        self.assertEquals(7, c)

    def test_2(self):
        arr = [2, 4, 6, 8, 9, 10, 14, 20]
        c = find_count_of_pairs(arr, 21)
        print(c)
        self.assertEquals(18, c)
