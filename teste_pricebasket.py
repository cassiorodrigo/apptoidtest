import unittest
from main import Cashier
from datetime import date
import sys


class ArgvArguments(object):
    def __enter__(self):
        lista_argumentos = [2,1,1,2]
        for e in lista_argumentos:
            sys.argv.append(e)
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.argv = [arg for arg in sys.argv]


class TestModel2(unittest.TestCase):

    def setUp(self):
        cart2 = []
        cart = "Apples Milk Bread soupsoup"
        cart1 = "PriceBasket ApplesMilkbread"
        cart3 = ""
        cart4 = 4
        self.new_cashier1 = Cashier.from_string(string_items=cart1, year_week=39)
        self.new_cashier = Cashier.from_string(cart, year_week=date.today().isocalendar()[1])
        self.new_cashier2 = Cashier(cart2, year_week='29')
        self.new_cashier3 = Cashier(cart3)
        self.new_cashier4 = Cashier.from_string(cart3)
        self.new_cashier5 = Cashier(["Soup", "Soup", "Soup"])
        with ArgvArguments() as avarg:
            self.arguments = avarg

    def tearDown(self):
        with ArgvArguments():
            self.arguments = []

    def test_stringparse(self):
        self.assertEqual(["Soup", "Soup", "Bread", "Milk", "Apples"], self.new_cashier.basket)
        self.assertEqual(['Bread', 'Milk', 'Apples'], self.new_cashier1.basket)
        self.assertEqual([], self.new_cashier3.basket)
        self.assertEqual([], self.new_cashier4.basket)
        self.assertRaises((TypeError, ValueError), Cashier.from_string,4, -1)
        self.assertRaises((TypeError, ValueError), Cashier.from_string,4, '30')
        self.assertRaises((TypeError, ValueError), Cashier.from_string)

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
        # self.assertEqual(0.0, self.new_cashier.apply_promotion().discount_apples)

    def test_from_sysarg(self):
        self.assertEqual(Cashier(['Soup', 'Soup', 'Bread', 'Milk', 'Apples', 'Apples']).__str__(), self.new_cashier.from_sysarg().__str__())

    def test_pass_list(self):
        self.assertEqual(["Soup", "Soup", "Soup"], self.new_cashier5)


if __name__ == "__main__":
    unittest.main()
