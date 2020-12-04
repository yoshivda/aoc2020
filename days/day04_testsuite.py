import unittest
from days.day04 import is_valid

class TestSuite(unittest.TestCase):

    def test_hgt(self):
        self.assertTrue(is_valid("hcl", ""))
