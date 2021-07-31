

class Cashier:
    stock = ["Soup", "Bread", "Milk", "Apples"]
    prices = [0.65, 0.80, 1.30, 1.0]
    product_price = dict(zip(stock,prices))
    basket = []
    def __init__(self, string_items):
        self.items_list = string_items.split(" ")
        for product in self.items_list:
            if product in self.stock:
                self.basket.append(product)

    def subtotal_calc(self):
        subtotal = float()
        for product in self.basket:
            subtotal += self.product_price[product]
        return subtotal


if __name__ == "__main__":
    new_cashier = Cashier("PriceBasket Apples Milk Bread")
    print(new_cashier.basket)
    print(new_cashier.subtotal_calc())