from locale import LC_ALL, setlocale
import re
from datetime import date
setlocale(LC_ALL, "en_ie")

class Cashier:
    stock = ["Soup", "Bread", "Milk", "Apples"]
    prices = [0.65, 0.80, 1.30, 1.0]
    product_price = dict(zip(stock, prices))
    basket = []

    def __init__(self, items_list, year_week=None):
        if year_week:
            if type(year_week) not in {int, str}:
                raise TypeError("year_week refers to the week number of the year"
                                "and should be an integer")
            self.year_week = int(year_week)
        for product in items_list:
            if product in self.stock:
                self.basket.append(product)

    @classmethod
    def from_string(cls, string_items):
        list_items = []
        for e in cls.stock:
            try:
                list_items.append(
                    string_items[re.search(e, string_items, re.IGNORECASE).span()[0]:re.search(
                        e, string_items, re.IGNORECASE).span()[1]].title())
            except Exception as err:
                print(err)
        return cls(list_items)

    def subtotal_calc(self):
        subtotal = 0.0
        for product in self.basket:
            subtotal += self.product_price[product]
        return subtotal

    @staticmethod
    def testedeteste():
        return 2

    def valid_promotion(self):
        this_week = date.today().isocalendar()[1]
        offer_apples = False
        offer_soup = False
        if self.year_week == this_week:
            offer_apples = True
        if self.basket.count("Soup") >= 2:
            offer_soup = True

        return offer_apples, offer_soup


if __name__ == "__main__":
    new_cashier = Cashier.from_string("PriceBasket Apples Milk Bread Soup")
    # new_cashier = Cashier(["PriceBasket", "Apples", "Milk", "Bread"])
    print(new_cashier.basket)
    print(new_cashier.subtotal_calc())