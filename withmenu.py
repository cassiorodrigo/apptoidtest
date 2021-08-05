import locale
import datetime
from locale import LC_ALL, setlocale

setlocale(LC_ALL, "en_ie")


class Cashier_menu:
    """
    creates a class that will create an cashier object 
    to manage items in the basket, prices and promotions
    On the object creation, user might want to pass the week number
    """

    def __init__(self, **kwargs):

        if kwargs.get("week_number"):
            apple_week = kwargs.get("week_number")
        else:
            apple_week = datetime.date.today().isocalendar()[1]

        if apple_week == datetime.date.today().isocalendar()[1]:
            self.apple_offer = True
        else:
            self.apple_offer = False

    basket_items = []
    basket_prices = []
    total = float()
    price = [{"index": 1, "product": "Soup", "price": 0.65}, {"index": 2, "product": "Bread", "price": 0.80},
             {"index": 3, "product": "Milk", "price": 1.30}, {"index": 4, "product": "Apple", "price": 1.00}]

    def __str__(self):
        return self.create_receipt()

    def new_cart(self):
        """
        create a new cart in the comand line via numeric options menu.
        number 0 finishes the insertion of items and put it forward to calculations
        :return: a list of items in the cart
        """
        text = str()
        for indexed_item in self.price:
            text += f"\n{indexed_item['index']}) {indexed_item['product']}"

        while True:
            try:
                item = int(input(f"""
                Which item would you like to add to chart?
                {text}
                Press 0 to when done adding items
                """))
                if item == 0:
                    break
                if item > 4:
                    print("Please, choose a number in the list")
                for product in self.price:
                    if product["index"] == item:
                        self.basket_items.append(product["product"])
                        self.basket_prices.append(product["price"])
            except ValueError:
                print("Please, choose a *number* in the list")

    def subtotal_calc(self):
        """
        Calculates the partial (subtotal) before conditions for promotions are checked
        and prices discounted
        :return: subtotal to be used to calculate the total if discounts are applicable
        """
        subtotal = float(0)
        for item_data in self.price:
            if item_data["product"] in self.basket_items:
                subtotal += item_data["price"] * self.basket_items.count(item_data["product"])

        return subtotal

    def check_promo_conditions(self, items_in_promo=None):
        """
        :param: list of items that will enable discounts this is acting as a place holder for next week if
        merchant wants to apply same discount principles for other items eg.: Milk
        This list should always have a len of 2.
        Soup – €0.65 per tin
        Bread – €0.80 per loaf
        Milk – €1.30 per bottle
        Apples – €1.00 per bag Current special offers are:
        Apples have 10% off their normal price this week
        Buy 2 tins of soup and get a loaf of bread for half price

        this method will generate a string to fill the receipt and compute discounts (if any) applicable
        to the current basket

        :return: text of discounted products and discount values for bread and apples
        """
        # For future implementation of promotions
        # Pass a list of prducts to receive discounts
        text_bread = ""
        discount_for_breads = 0
        text_apple = ""
        discount_apples = 0

        if items_in_promo is None:
            items_in_promo = ["Apple", "Soup"]
        if self.apple_offer:
            discount_for_apples = '10%'
        else:
            discount_for_apples = ''

        if items_in_promo[0] in self.basket_items:
            if self.apple_offer:
                discount_apples = self.basket_items.count(items_in_promo[0]) * 0.1
                text_apple = f"{items_in_promo[0]} {discount_for_apples} off: -{locale.currency(discount_apples)}"
        else:
            text_apple = ""
            discount_apples = 0
        if self.basket_items.count(items_in_promo[1]) >= 2:
            if "Bread" in self.basket_items:
                for each in self.price:
                    if each["product"] == "Bread":
                        discount_for_breads = each["price"]/2
                        text_bread = f"A loaf of bread: -{locale.currency(discount_for_breads)}"

        text_receipt = f"{text_apple}\n{text_bread}"

        if text_apple == "" and text_bread == "":
            text_receipt = "no offers available"

        return text_receipt, discount_for_breads, discount_apples

    def sum_it_up(self):
        """
        This will calculate the prices for the total, subtracting the discounted products.
        It helps generating part of the receipt to be passed to the receipt generator method (create_receipts)
        :return: the result of subtotal -
        """

        subtotal = self.subtotal_calc()
        text_offers, discount_breads, discount_apples = self.check_promo_conditions()

        total = subtotal - discount_breads - discount_apples

        return text_offers, total

    def create_receipt(self):

        full_receipt, total = self.sum_it_up()
        print(f"Subtotal: {locale.currency(self.subtotal_calc())}")
        print(full_receipt, "Total: ", locale.currency(total))
        full_receipt = "\n".join(self.basket_items)

        return full_receipt


if __name__ == "__main__":
    new_cashier = Cashier_menu()
    produtos = new_cashier.new_cart()
    receipt = new_cashier.create_receipt()
    print(receipt)

