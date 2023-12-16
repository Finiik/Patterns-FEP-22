class ShoppingCart:
    def __init__(self, item, amount):
        self.item = item
        self.amount = amount


class Order(ShoppingCart):
    def __init__(self, item, amount, item_price, shipment_price):
        super().__init__(item, amount)
        self.item_price = item_price
        self.shipment_price = shipment_price

    def total_price(self):
        return self.item_price * self.amount + self.shipment_price