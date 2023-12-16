class Payment:
    def __init__(self, card_balance, total_price):
        self.card_balance = card_balance
        self.total_price = total_price

    def verify_payment(self):
        if self.total_price > self.card_balance:
            return False

    def update_balance(self):
        new_balance = self.card_balance - self.total_price
        return new_balance