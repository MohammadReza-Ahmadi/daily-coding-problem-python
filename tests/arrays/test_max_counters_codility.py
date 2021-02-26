from unittest import TestCase

from src.arrays.max_counters_codility import get_counters_correct


class Test(TestCase):
    def test_get_counters_1(self):
        A = [3, 4, 4, 6, 1, 4, 4]
        e = [3, 2, 2, 4, 2]
        N = 5
        r = get_counters_correct(N, A)
        print('correct={}'.format(r))
        self.assertEquals(e, r)

    def test_get_counters_2(self):
        A = [5, 1, 3, 3, 9, 7, 1]
        N = 5
        e = [3, 2, 2, 2, 2]
        r = get_counters_correct(N, A)
        self.assertEquals(e, r)

    def test_get_counters_3(self):
        A = [5, 1, 3, 3, 9, 7, 1, 8]
        N = 5
        e = [3, 3, 3, 3, 3]
        r = get_counters_correct(N, A)
        self.assertEquals(e, r)

    def test_get_counters_4(self):
        A = [22, 1, 12, 3, 16, 7, 20, 30, 12, 2]
        N = 8
        e = [3, 4, 3, 3, 3, 3, 3, 3]
        r = get_counters_correct(N, A)
        self.assertEquals(e, r)
