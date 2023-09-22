""""""


class Bill:
    """Holds bill implementation details.
    """

    def __init__(self, customer_id: int, limit: float=100) -> None:
        self.limit = limit
        self.customer_id = customer_id
        self.current_debt = 0

    def __repr__(self) -> str:
        return f"Bill(limit={self.limit}, current_debt={self.current_debt}, customer_id={self.customer_id})"

    def pay(self, value: float) -> None:
        temp = self.current_debt - value
        if temp < 0:
            self.current_debt = 0
        else:
            self.current_debt = temp
        print(f"Customer {self.customer_id} paid {value}")

    def add(self, debt: float) -> None:
        temp = self.current_debt + debt
        if temp <= self.limit:
            self.current_debt = temp
            print(f"Add {temp} to debt")
        else:
            print(f"You reached the limit. Operation is forbidden")

    def change_limit(self, value: float) -> None:
        self.limit += value
        print(f"Limit has been risen to {self.limit}")
