class Stock:
    def __init__(self, item, amount, stock):
        self.item = item
        self.amount = amount
        self.stock = stock

    def check_stock(self):
        if self.stock >= self.amount:
            new_stock = self.stock - self.amount
            return new_stock
        else:
            return None