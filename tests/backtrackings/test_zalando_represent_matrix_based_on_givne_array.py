from unittest import TestCase

from src.backtrackings.zalando_represent_matrix_based_on_givne_array import get_matrix


class Test(TestCase):
    def test_get_matrix_1(self):
        arr = [0, 0, 1, 1, 2]
        u = 2
        l = 3
        m = get_matrix(u, l, arr)
        print(m)

    def test_get_matrix_2(self):
        arr = [2, 0, 2, 0]
        u = 2
        l = 2
        m = get_matrix(u, l, arr)
        print(m)

    def test_get_matrix_3(self):
        arr = [2, 0, 1, 2, 1, 0, 0, 2, 0, 1]
        u = 4
        l = 5
        m = get_matrix(u, l, arr)
        print(m)
