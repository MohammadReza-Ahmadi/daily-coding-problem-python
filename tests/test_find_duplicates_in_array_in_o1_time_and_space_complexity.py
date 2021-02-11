from unittest import TestCase

from src.arrays.find_duplicates_in_array_in_o1_time_complexity import find_duplicates


class Test(TestCase):
    def test_find_duplicates(self):
        array = [1, 2, 3, 1, 3, 6, 6]
        dup = find_duplicates(array)
        if bool(dup):
            s = ''
            for a in dup:
                s = a + ', '
            print(s)
