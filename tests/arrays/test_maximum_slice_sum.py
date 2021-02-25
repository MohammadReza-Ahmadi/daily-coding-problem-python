from unittest import TestCase

from src.arrays.maximum_slice_sum import get_max_slice_sum


class Test(TestCase):
    def test_get_max_slice_1(self):
        arr = [5, -7, 3, 5, -2, 4, -1]
        r = get_max_slice_sum(arr)
        self.assertEquals(10, r)

    def test_get_max_slice_2(self):
        arr = [5]
        r = get_max_slice_sum(arr)
        self.assertEquals(5, r)

    def test_get_max_slice_3(self):
        arr = [-10]
        r = get_max_slice_sum(arr)
        self.assertEquals(-10, r)

    def test_get_max_slice_4(self):
        arr = [-10, -2]
        r = get_max_slice_sum(arr)
        self.assertEquals(-2, r)

    def test_get_max_slice_5(self):
        arr = [-10, -2, -3]
        r = get_max_slice_sum(arr)
        self.assertEquals(-2, r)

    def test_get_max_slice_6(self):
        arr = [-10, -11]
        r = get_max_slice_sum(arr)
        self.assertEquals(-10, r)

    def test_get_max_slice_7(self):
        arr = [1, 2]
        r = get_max_slice_sum(arr)
        self.assertEquals(3, r)

    def test_get_max_slice_8(self):
        arr = [1, -2]
        r = get_max_slice_sum(arr)
        self.assertEquals(1, r)

    def test_get_max_slice_9(self):
        arr = [-1, 1]
        r = get_max_slice_sum(arr)
        self.assertEquals(1, r)
