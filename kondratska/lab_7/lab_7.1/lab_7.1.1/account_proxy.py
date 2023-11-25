from account import IAcct


class AccountProxy(IAcct):
    def __init__(self, real_account, account_number):
        super().__init__()
        self.real_account = real_account
        self.account_number = account_number

    def account_number(self):
        return self.real_account.account_number

    def get_balance(self) -> float:
        return self.real_account.get_balance()

    def withdraw(self, withdrawn_amount: float) -> bool:
        return self.real_account.withdraw(withdrawn_amount)
