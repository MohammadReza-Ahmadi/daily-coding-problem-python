import unittest

from src.arrays import pythagorean_triplet_in_an_array


class TestPythagoreanTripletInAnArray(unittest.TestCase):
    def test_5_true(self):
        c = pythagorean_triplet_in_an_array.PythagoreanTripletInAnArray()
        array = [3, 1, 4, 6, 5]
        expected = True
        result = c.find_triplet(array)
        self.assertEqual(expected, result)

    def test_8_true(self):
        c = pythagorean_triplet_in_an_array.PythagoreanTripletInAnArray()
        array = [3, 1, 2, 4, 1, 6, 11, 5]
        expected = True
        result = c.find_triplet(array)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
