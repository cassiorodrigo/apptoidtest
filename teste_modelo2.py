import unittest
from modelo2 import Cashier


class TestModel2(unittest.TestCase):

    def setUp(self):
        stock = ["Soup", "Bread", "Milk", "Apples"]
        cart1 = "Apples Milk Bread"
        cart2 = "PriceBasket Apples Milk Bread"
        # self.new_cashier = Cashier(string_items=cart2)
        self.new_cashier = Cashier.from_string(cart2)

    def tearDown(self):
        pass

    def test_subtotal(self):

        self.assertAlmostEqual(3.1, self.new_cashier.subtotal_calc(), 2)

    def test_testedeteste(self):
        self.assertEqual(2, self.new_cashier.testedeteste())


if __name__ == "__main__":
    unittest.main()

