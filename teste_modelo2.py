import unittest
from modelo2 import Cashier


class TestModel2(unittest.TestCase):

    def setUp(self):
        stock = ["Soup", "Bread", "Milk", "Apples"]
        cart2 = []
        cart = "Apples Milk Bread soupsoup"
        cart1 = "PriceBasket ApplesMilkbread"
        self.new_cashier1 = Cashier.from_string(string_items=cart1, year_week=39)
        self.new_cashier = Cashier.from_string(cart, year_week=30)
        self.new_cashier2 = Cashier(cart2, year_week=29)

    def tearDown(self):
        pass

    def test_stringparse(self):
        self.assertEqual(["Soup", "Soup", "Bread", "Milk", "Apples"], self.new_cashier.basket)

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

if __name__ == "__main__":
    unittest.main()

