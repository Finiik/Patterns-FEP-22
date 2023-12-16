from abc import ABC, abstractmethod
from typing import Optional, Tuple


class IAcct(ABC):
    @abstractmethod
    def get_balance(self) -> float:
        pass

    @abstractmethod
    def withdraw(self, withdrawn_amount: float) -> bool:
        pass


class Account(IAcct):
    def __init__(self, account_number: str, amount: float):
        super().__init__()
        self.account_number = account_number
        self.amount = amount

    def get_balance(self) -> float:
        return self.amount

    def withdraw(self, withdrawn_amount: float) -> Tuple[float, bool]:
        if withdrawn_amount <= self.amount:
            self.amount -= withdrawn_amount
            return self.amount, True
        else:
            print("Insufficient funds.")
            return self.amount, False


