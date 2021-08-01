import unittest
from modelo2 import Cashier


class TestModel2(unittest.TestCase):

    def setUp(self):
        cart2 = []
        cart = "Apples Milk Bread soupsoup"
        cart1 = "PriceBasket ApplesMilkbread"
        cart3 = ""
        cart4 = 4
        self.new_cashier1 = Cashier.from_string(string_items=cart1, year_week=39)
        self.new_cashier = Cashier.from_string(cart, year_week=30)
        self.new_cashier2 = Cashier(cart2, year_week=29)
        self.new_cashier3 = Cashier(cart3)
        self.new_cashier4 = Cashier.from_string(cart3)
        # self.new_cashier5 = Cashier.from_string(4, year_week=-1)
        self.new_cashier5 = Cashier.from_string("soup soup bread", year_week=-1)

    def tearDown(self):
        pass

    def test_stringparse(self):
        self.assertEqual(["Soup", "Soup", "Bread", "Milk", "Apples"], self.new_cashier.basket)
        self.assertEqual(['Bread', 'Milk', 'Apples'], self.new_cashier1.basket)
        self.assertEqual([], self.new_cashier3.basket)
        self.assertEqual([], self.new_cashier4.basket)
        self.assertRaises((TypeError, ValueError), self.new_cashier5)

    def test_subtotal(self):

        self.assertAlmostEqual(4.4, self.new_cashier.subtotal_calc(), 2)
        self.assertAlmostEqual(3.1, self.new_cashier1.subtotal_calc(), 2)
        self.assertAlmostEqual(0, self.new_cashier2.subtotal_calc(), 2)

    def test_valid_promotion(self):
        valid_apple, valid_offer = self.new_cashier.valid_promotion()
        self.assertTrue(valid_apple)
        self.assertTrue(valid_offer)
        valid_apple, valid_offer = self.new_cashier1.valid_promotion()
        self.assertFalse(valid_apple)
        self.assertFalse(valid_offer)
        valid_apple, valid_offer = self.new_cashier2.valid_promotion()
        self.assertFalse(valid_apple)
        self.assertFalse(valid_offer)

    def test_apply_promotion(self):
        self.assertAlmostEqual(3.9, self.new_cashier.apply_promotion()[0], 2)
        self.assertAlmostEqual(0.1, self.new_cashier.apply_promotion()[1], 2)
        self.assertAlmostEqual(0.0, self.new_cashier1.apply_promotion()[1], 2)
        self.assertAlmostEqual(0.4, self.new_cashier.apply_promotion()[2], 2)


if __name__ == "__main__":
    unittest.main()

