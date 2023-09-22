class Bill:
    """Holds bill implementation details."""

    def __init__(self, limit, currDebt=0) -> None:
        self.limit = limit
        self.current_debt = currDebt

    def __str__(self) -> str:
        return f"Bill: limit: {self.limit}, current debt: {self.current_debt})"

    def pay(self, value: float) -> None:
        temp = self.current_debt - value
        if temp < 0:
            self.current_debt = 0
        else:
            self.current_debt = temp

    def add(self, debt: float) -> None:
        temp = self.current_debt + debt
        if temp < self.limit:
            self.current_debt = temp
            print(f"Add {temp} to debt")
        else:
            raise ValueError(f"You reached the limit. Operation is forbidden")

    def check_limit(self):
        return f"Your current limit is {self.current_debt}"

    def change_limit(self, value: float) -> None:
        self.limit += value
        print(f"Limit has been changed to {self.limit}")
