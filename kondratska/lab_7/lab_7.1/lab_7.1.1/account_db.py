from abc import ABC, abstractmethod
from account import IAcct, Account
from typing import Optional, Dict


class IDB(ABC):
    @abstractmethod
    def get_account(self, account_number):
        pass

    @abstractmethod
    def login(self, account_number) -> Optional['IAcct']:
        pass

    @abstractmethod
    def logout(self, account: IAcct):
        pass


class AccountDatabase(IDB):
    def __init__(self):
        self.accounts: Dict[str, Account] = {}

    def get_account(self, account_number: str) -> Optional[IAcct]:
        return self.accounts.get(account_number)

    def create_account(self, account_number: str, amount: float):
        account = Account(account_number, amount)
        self.accounts[account_number] = account

    def login(self, account_number: str) -> Account:
        return self.accounts.get(account_number)

    def logout(self, account_number: str):
        if account_number in self.accounts:
            self.accounts.popitem()
            print(f"Logout successful for account {account_number}")
        else:
            print(f"Account {account_number} not found during logout.")
