from unittest import TestCase

from src.arrays.check_for_pair_of_given_sum_in_array import CheckForPairByGivenSumInAnArray


class Test(TestCase):
    def test_4_false_m1(self):
        c = CheckForPairByGivenSumInAnArray()
        arr = [1, 4, 45, 6, 10, -8]
        self.assertFalse(c.has_pair_m1(arr, 20))

    def test_4_true_m1(self):
        c = CheckForPairByGivenSumInAnArray()
        arr = [1, 4, 45, 6, 10, -8]
        self.assertTrue(c.has_pair_m1(arr, 16))

    def test_4_false_m2(self):
        c = CheckForPairByGivenSumInAnArray()
        arr = [1, 4, 45, 6, 10, -8]
        self.assertFalse(c.has_pair_m2(arr, 20))

    def test_4_true_m2(self):
        c = CheckForPairByGivenSumInAnArray()
        arr = [1, 4, 45, 6, 10, -8]
        self.assertTrue(c.has_pair_m2(arr, 16))
