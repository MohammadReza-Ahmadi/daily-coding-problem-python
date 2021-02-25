from unittest import TestCase

from src.dynamic_programmings.get_longest_increasing_subsequence import get_longest_subsequence


class Test(TestCase):
    def test_get_longest_subsequence(self):
        arr = [10, 22, 9, 33, 21, 50, 41, 60]
        mx = get_longest_subsequence(arr)
        print(mx)