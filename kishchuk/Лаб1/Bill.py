class Bill:
    def __init__(self, limiting_amount):
        self.limiting_amount = limiting_amount
        self.current_debt = 0.0

    def check(self, amount):
        return self.current_debt + amount <= self.limiting_amount

    def add(self, amount):
        self.current_debt += amount

    def pay(self, amount):
        self.current_debt -= amount

    def change_the_limit(self, amount):
        self.limiting_amount = amount