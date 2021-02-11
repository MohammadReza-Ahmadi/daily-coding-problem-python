from unittest import TestCase

from src.arrays.find_lost_element_from_duplicated_array import m1_find_missing_element_by_binary_search, \
    m2_find_missing_element_by_binary_search


class Test(TestCase):
    def test_m1_find_missing_element_by_binary_search(self):
        arr1 = [1, 4, 5, 7, 9]
        arr2 = [4, 5, 7, 9]
        ret = m1_find_missing_element_by_binary_search(arr1, arr2, 0, 0, (len(arr1) - 1), (len(arr2) - 1))
        print('ret={}'.format(ret))
        self.assertEquals(ret, 1)

        arr1 = [1, 4, 5, 7, 9]
        arr2 = [1, 4, 5, 9]
        ret = m1_find_missing_element_by_binary_search(arr1, arr2, 0, 0, (len(arr1) - 1), (len(arr2) - 1))
        print('ret={}'.format(ret))
        self.assertEquals(ret, 7)

        arr1 = [1, 4, 5, 7, 9, 11, 13, 14, 15, 20, 22]
        arr2 = [1, 4, 5, 7, 9, 11, 13, 14, 15, 22]
        # ret = m1_find_missing_element_by_binary_search(arr1, arr2, 0, 0, (len(arr1) - 1), (len(arr2) - 1))
        ret = m2_find_missing_element_by_binary_search(arr1, arr2, 0, (len(arr1) - 1))
        print('ret={}'.format(ret))
        # self.assertEquals(ret, 20)
