from coe_number.cat_mouse import Cat_and_Mouse
import unittest

class CatMouseTest(unittest.TestCase):
    def test_give_1_2_3_should_CatB(self):
        self.assertEqual(Cat_and_Mouse(1, 2, 3), "Cat B")

    def test_give_1_3_2_should_MouseC(self):
        self.assertEqual(Cat_and_Mouse(1, 3, 2), "Mouse C")

    def test_give_1_5_4_should_CatB(self):
        self.assertEqual(Cat_and_Mouse(1, 5, 4), "Cat B")

    def test_give_10_20_15_should_MouseC(self):
        self.assertEqual(Cat_and_Mouse(10, 20, 15), "Mouse C")

    def test_give_0_0_0_should_MouseC(self):
        self.assertEqual(Cat_and_Mouse(0, 0, 0), "Mouse C")

    def test_give_negative_positions_should_MouseC(self):
        self.assertEqual(Cat_and_Mouse(-5, -1, -3), "Mouse C")

    def test_give_4_8_5_should_CatA(self):
        self.assertEqual(Cat_and_Mouse(4, 8, 5), "Cat A")