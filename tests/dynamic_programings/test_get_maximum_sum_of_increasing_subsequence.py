from unittest import TestCase

from src.dynamic_programmings.get_maximum_sum_of_increasing_subsequence import get_maximum_sum_of_subsequence


class Test(TestCase):
    def test_get_maximum_sum_of_subsequence_106(self):
        arr = [1, 101, 2, 3, 100, 4, 5]
        max_sum = get_maximum_sum_of_subsequence(arr)
        print(max_sum)
        self.assertEquals(106, max_sum)

    def test_get_maximum_sum_of_subsequence_22(self):
        arr = [3, 4, 5, 10]
        max_sum = get_maximum_sum_of_subsequence(arr)
        print(max_sum)
        self.assertEquals(22, max_sum)

    def test_get_maximum_sum_of_subsequence_10(self):
        arr = [10, 5, 4, 3]
        max_sum = get_maximum_sum_of_subsequence(arr)
        print(max_sum)
        self.assertEquals(10, max_sum)
