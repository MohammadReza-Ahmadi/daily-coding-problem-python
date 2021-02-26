from unittest import TestCase

from src.arrays.tape_equilibrium_codility import get_minimal_difference


class Test(TestCase):
    def test_get_minimal_difference_1(self):
        A = [3, 1, 2, 4, 3]
        r = get_minimal_difference(A)
        self.assertEquals(1, r)
