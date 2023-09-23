class Bill:
    """Holds bill implementation details."""

    def __init__(self, limiting_amount: float = 500, operator_id: int = 0) -> None:  # конструкторк клас bill,
        # приймає один параметр limiting_amount(обмежену суму, яку користувач може витратити)
        self.limiting_amount = limiting_amount
        self.operator_id = operator_id
        self.currentDebt = 0

    def check(self, amount: float) -> bool:  # приймає параметр amount(суму,яку користувач може додати до свого боргу)
        return (self.currentDebt + amount) <= self.limiting_amount  # якщо виконується умова, то можна додати суму
        # без перевищення боргу

    def add(self, amount: float) -> None:  # додавання боргів до рахунку
        self.currentDebt += amount

    def pay(self, amount: float) -> None:  # оплата рахунків
        self.currentDebt -= amount  # віднімає певну суму грошей від боргу
        if self.currentDebt < 0:  # якщо результат менший за 0 - борг погашено
            self.currentDebt = 0  # то борг = 0

    def change_limit(self, new_limit: float) -> None:  # зміна обмеження(ліміту)
        self.limiting_amount = new_limit
