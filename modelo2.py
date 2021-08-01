from locale import LC_ALL, setlocale, currency
import re
from datetime import date
setlocale(LC_ALL, "en_ie")


class Cashier:
    """
    Creates an cashier object. It requires either a list on the object creation
    or a string containing the name of the products passed through
    Cashier.from_string(<string in here>).

    :example:
    Usage examples passing a string:
    new_cashier = Cashier.from_string("PriceBasket Apples Milk bread Soupsoup", year_week=30)
    print(new_cashier)

    or a list:

    new_cashier1 = Cashier(["PriceBasket", "Apples", "Milk", "Bread"])
    print(new_cashier1)

    print method was rewritten to print the receipt itself.
    repr method as standards



    """
    stock = ["Soup", "Bread", "Milk", "Apples"]
    prices = [0.65, 0.80, 1.30, 1.0]
    product_price = dict(zip(stock, prices))

    def __init__(self, items_list, year_week=None):
        self.items_string = " "
        self.basket = []
        self.items_list = items_list
        if year_week:
            if type(year_week) not in {int, str}:
                raise TypeError("year_week refers to the week number of the year"
                                "and should be an integer")
            self.year_week = int(year_week)
        for product in items_list:
            if product in self.stock:
                self.basket.append(product)
        self.items_string = self.items_string.join(str(e) for e in self.basket)

    def __repr__(self):
        return f"Cashier({self.items_list})"

    def __str__(self):
        total, discount_apples, discount_bread = self.apply_promotion()
        items_descriptions = "\n\t".join(self.basket)
        if discount_apples > 0 or discount_bread > 0:
            offers_active = f'''
            Offers active:
            Apples: -{currency(discount_apples)}
            Soup: -{currency(discount_bread)}'''

        else:
            offers_active = "(No offers avilable)"
        descriptive = f'''
        
Products in the basket: {self.items_string}
Subtotal: {currency(self.subtotal_calc())}
{offers_active}
Total: {currency(total)}
Items:
\t{items_descriptions}
'''
        return descriptive

    @classmethod
    def from_string(cls, string_items, year_week=None):
        if year_week is not None:
            if type(string_items) != str:
                raise TypeError("Please, pass a string to this classmethod")
            if type(year_week) != int and year_week < 0:
                raise ValueError("Week must be a positive integer")
        list_items = []
        for e in cls.stock:
            matches = re.finditer(e, string_items, re.IGNORECASE)
            for match in matches:
                try:
                    list_items.append(string_items[match.span()[0]:match.span()[1]].title())
                except Exception as err:
                    print(err)
        return cls(list_items, year_week)

    def subtotal_calc(self):
        """
        Calculates the partial (subtotal) before conditions for promotions are checked
        and prices discounted

        :return:Float result of the sum of products in the cart before discounts.
        """

        subtotal = 0.0
        for product in self.basket:
            subtotal += self.product_price[product]
        return subtotal

    def valid_promotion(self):
        """
        Since apples offer depends on the week number, it assumes the offer is no long valid if no year_week number
        is passed.
        :return: Tuple with 2 Boolean values being the first True for apples offer active
        and the second True for soup offer active. If either is not active, the returned value will be False
        """
        this_week = date.today().isocalendar()[1]
        offer_apples = False
        offer_soup = False
        try:
            if self.year_week == this_week:
                offer_apples = True
        except AttributeError as aterror:
            print(aterror)
            print('As no week number was passed, Apples offer will be turned off')

        if self.basket.count("Soup") >= 2:
            offer_soup = True
        return offer_apples, offer_soup

    def apply_promotion(self, apple_discount_rate=0.1):
        """
        This method takes no arguments and apply offers discounts on the subtotal.
        :return: a total float with applied discounts if any
        """
        discount_apples = 0.0
        discount_bread = 0.0
        offer_apples, offer_soup = self.valid_promotion()
        if offer_apples:
            discount_apples = self.basket.count("Apples")*(apple_discount_rate*self.product_price["Apples"])
        if offer_soup:
            soup_discounts_possible = self.basket.count("Soup")//2
            number_of_breadloaf = self.basket.count("Bread")
            n_discounted_bread = 0
            for n in range(soup_discounts_possible):
                if n <= number_of_breadloaf:
                    n_discounted_bread += 1
            discount_bread = n_discounted_bread * (self.product_price["Bread"]/2)

        total = self.subtotal_calc() - discount_apples - discount_bread
        return total, discount_apples, discount_bread


if __name__ == "__main__":
    new_cashier = Cashier.from_string("PriceBasket Apples Milk bread Soupsoup", year_week=30)
    new_cashier1 = Cashier(["PriceBasket", "Apples", "Milk", "Bread"])
    print(new_cashier1)


