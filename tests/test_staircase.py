from coe_number.staircase import StairCase
import unittest

class StairCaseTest(unittest.TestCase):
    def test_give_2_with_hash_should_be_hh(self):
        n = 2
        pattern = "#"
        expected_output = "#\n##"
        result = StairCase(n, pattern)
        self.assertEqual(result, expected_output, f"Should be {expected_output}")

    def test_give_3_with_star_should_be_star_starstar_starstarstar(self):
        n = 3
        pattern = "*"
        expected_output = "*\n**\n***"
        result = StairCase(n, pattern)
        self.assertEqual(result, expected_output, f"Should be {expected_output}")

    def test_give_1_with_plus_should_be_plus(self):
        n = 1
        pattern = "+"
        expected_output = "+"
        result = StairCase(n, pattern)
        self.assertEqual(result, expected_output, f"Should be {expected_output}")

    def test_give_0_with_hash_should_be_empty(self):
        n = 0
        pattern = "#"
        expected_output = ""
        result = StairCase(n, pattern)
        self.assertEqual(result, expected_output, f"Should be {expected_output}")

    def test_give_4_with_dollar_should_be_dollar_dollardollar_dollardollardollar_dollardollardollardollar(self):
        n = 4
        pattern = "$"
        expected_output = "$\n$$\n$$$\n$$$$"
        result = StairCase(n, pattern)
        self.assertEqual(result, expected_output, f"Should be {expected_output}")