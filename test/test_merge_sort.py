import unittest

from src.sorting.merge_sort import sorting


class TestMergeSort(unittest.TestCase):
    def test_1(self):
        arr = [20, 35, -15, 7, 55, 1, -22]
        sorting(arr, 0, len(arr))
        print(arr, end=" ")


if __name__ == '__main__':
    unittest.main()
