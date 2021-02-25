from unittest import TestCase

from src.recursions.davis_staircase_by_recursions import step_perms_by_recursion


class Test(TestCase):
    def test_step_perms_by_recursion_1(self):
        n = 3
        r = step_perms_by_recursion(n)
        self.assertEquals(r, 4)

    def test_step_perms_by_recursion_2(self):
        n = 7
        r = step_perms_by_recursion(n)
        self.assertEquals(r, 44)

    def test_step_perms_by_recursion_3(self):
        n = 5
        r = step_perms_by_recursion(n)
        self.assertEquals(r, 13)

    def test_step_perms_by_recursion_4(self):
        n = 8
        r = step_perms_by_recursion(n)
        self.assertEquals(r, 81)




