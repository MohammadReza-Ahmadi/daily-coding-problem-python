from unittest import TestCase

from src.dynamic_programmings.davis_staircase_by_dynamic_programming import step_perms_by_dynamic_programming


class Test(TestCase):
    def test_step_perms_by_dynamic_programming_1(self):
        n = 3
        r = step_perms_by_dynamic_programming(n)
        self.assertEquals(r, 4)

    def test_step_perms_by_dynamic_programming_2(self):
        n = 7
        r = step_perms_by_dynamic_programming(n)
        self.assertEquals(r, 44)

    def test_step_perms_by_dynamic_programming_3(self):
        n = 5
        r = step_perms_by_dynamic_programming(n)
        self.assertEquals(r, 13)

    def test_step_perms_by_dynamic_programming_4(self):
        n = 8
        r = step_perms_by_dynamic_programming(n)
        self.assertEquals(r, 81)
