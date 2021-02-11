import unittest

import src.arrays.print_missing_element_lie_range_0_to_99 as target


class TestPrintMissingElement(unittest.TestCase):
    def test_get_missing_numbers(self):
        array = [88, 105, 3, 2, 200, 0, 10]
        target.get_missing_numbers(array)


if __name__ == '__main__':
    unittest.main()
