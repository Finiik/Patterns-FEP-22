class Bill:
    """Holds bill implementation details."""

    def __init__(self, limiting_amount: float = 500, operator_id: int = 0) -> None:
        self.limiting_amount = limiting_amount
        self.operator_id = operator_id
        self.currentDebt = 0

    def check(self, amount: float) -> bool:
        return (self.currentDebt + amount) <= self.limiting_amount

    def add(self, amount: float) -> None:
        self.currentDebt += amount

    def pay(self, amount: float) -> None:
        self.currentDebt -= amount
        if self.currentDebt < 0:
            self.currentDebt = 0

    def change_limit(self, new_limit: float) -> None:
        self.limiting_amount = new_limit
