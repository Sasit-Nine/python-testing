from coe_number.two_characters import alternate
import unittest

class TestTwoCharacters(unittest.TestCase):
    def test_give_helloworld_return_3(self):
        self.assertEqual(alternate("helloworld"), 3)

    def test_giveababab_return_6(self):
        self.assertEqual(alternate("ababab"), 6)

    def test_givezzz_return_0(self):
        self.assertEqual(alternate("zzz"), 0)

    def test_give_xy_return_2(self):
        self.assertEqual(alternate("xy"), 2)

    def test_give_abcdefabc_return_4(self):
        self.assertEqual(alternate("abcdefabc"), 4)

