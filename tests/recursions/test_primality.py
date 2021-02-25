from unittest import TestCase

from src.recursions.primality import primality


class Test(TestCase):
    def test_primality_1(self):
        r = primality(602)
        self.assertEquals(r, 'Not prime')

    def test_primality_2(self):
        r = primality(601)
        self.assertEquals(r, 'Prime')

    def test_primality_3(self):
        r = primality(929)
        self.assertEquals(r, 'Prime')

    def test_primality_4(self):
        r = primality(921)
        self.assertEquals(r, 'Not prime')

    def test_primality_5(self):
        r = primality(1)
        self.assertEquals(r, 'Not prime')

    def test_primality_6(self):
        r = primality(2)
        self.assertEquals(r, 'Prime')

    def test_primality_7(self):
        r = primality(1000000007)
        self.assertEquals(r, 'Prime')
