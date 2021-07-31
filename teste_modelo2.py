import unittest
import modelo2


class TestModel2(unittest.TestCase):

    def setUp(self):
        stock = ["Soup", "Bread", "Milk", "Apples"]
        cart1 = "Apples Milk Bread"
        cart2 = "PriceBasket Apples Milk Bread"
        self.new_cashier = modelo2.Cashier(string_items=cart2)

    def tearDown(self):
        pass

    def test_initial(self):
        self.assertIs(type(self.new_cashier.items_list), list)
        self.assertIs(type(self.new_cashier.product_price), dict)
        self.assertIn("Soup", self.new_cashier.product_price)
        self.assertIn("Milk", self.new_cashier.product_price)
        self.assertNotIn("PriceBasket", self.new_cashier.basket)
        self.assertEqual(3, len(self.new_cashier.basket))

    def test_subtotal(self):
        TestModel2().assertAlmostEqual(3.1, self.new_cashier.subtotal_calc(), 2)


if __name__ == "__main__":
    unittest.main()

