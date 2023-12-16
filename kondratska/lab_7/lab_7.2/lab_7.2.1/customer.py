from typing import List
from account_proxy_1 import AccountProxy


class Customer:
    def __init__(self, name, account_number):
        self.name = name
        self.account_number = account_number
        self.attached_accounts: List[AccountProxy] = []

    def attach_customer(self, account: AccountProxy):
        if account not in self.attached_accounts:
            self.attached_accounts.append(account)
        else:
            return self.attached_accounts

    def detach_customer(self, account: AccountProxy):
        if account not in self.attached_accounts:
            self.attached_accounts.remove(account)
        else:
            return self.attached_accounts

    def notify(self, account_proxy: AccountProxy) -> None:
        print(f"Notification for {self.name}: Balance updated - {account_proxy.get_balance()}")

    def withdraw(self, withdrawn_amount: float) -> bool:
        self.notify()
        return self.account_number.withdraw(withdrawn_amount)