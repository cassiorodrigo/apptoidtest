import unittest
from withmenu import Cashier
from unittest.mock import patch


class TestBasket(unittest.TestCase):

    def setUp(self):
        self.cashier = Cashier(week_number=30)
        self.cashier2 = Cashier(week_number=29)
        self.cashier.basket_items = ["Soup", "Soup", "Bread", "Milk", "Apple"]
        self.cashier2.basket_items = ["Soup", "Bread", "Bread", "Milk", "Apple"]

    def tearDown(self):
        pass

    def test_new_basket(self):
        TestBasket().assertEqual(self.cashier.apple_offer, True)
        TestBasket().assertEqual(self.cashier2.apple_offer, False)
        TestBasket().assertIs(type(self.cashier.basket_items), list)

    def test_subtotal(self):
        TestBasket().assertEqual(self.cashier.subtotal_calc(), 4.4)
        TestBasket().assertEqual(self.cashier2.subtotal_calc(), 4.55)

    def test_check_promo_conditions(self):
        TestBasket().assertEqual(self.cashier.check_promo_conditions(), )




if __name__ == "__main__":
    unittest.main()

