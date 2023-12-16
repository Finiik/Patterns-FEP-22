from typing import List
from customer import Customer
from account_1 import IAcct


class AccountProxy(IAcct):
    def __init__(self, real_account, account_number):
        super().__init__()
        self.real_account = real_account
        self.account_number = account_number
        self.customers = List['Customer'] = []

    def attach_customer(self, customer: Customer):
        if customer not in self.customers:
            self.attach_customer(customer)

    def detach_customer(self, customer: Customer):
        if customer in self.customers:
            self.detach_customer(customer)

    def notify_customer(self):
        cust_list = self.customers
        for customer in cust_list:
            customer.notify()

    def account_number(self):
        return self.real_account.account_number

    def get_balance(self) -> float:
        return self.real_account.get_balance()

    def withdraw(self, withdrawn_amount: float) -> bool:
        self.notify_customer()
        return self.real_account.withdraw(withdrawn_amount)
