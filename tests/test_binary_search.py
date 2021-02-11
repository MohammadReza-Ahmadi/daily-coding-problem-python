from unittest import TestCase

from src.arrays.binary_search import binary_search


class Test(TestCase):
    def test_binary_search(self):
        array = [2, 3, 5, 7, 8, 10, 11, 12, 14, 15, 20, 23, 29, 33, 35, 36, 40]
        ret = binary_search(array, 0, (len(array) - 1), 15)
        print('ret={}'.format(ret))
