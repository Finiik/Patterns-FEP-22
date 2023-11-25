from account_proxy import AccountProxy
from account_db import AccountDatabase


class ATMController:
    def __init__(self, account_database: AccountDatabase, account_number: str, amount: float):
        self.account_proxy = AccountProxy(account_database.login(account_number), account_number)
        self.account_database = account_database
        self.account_number = account_number
        self.amount = amount
        self.login_status = False

    def handle_balance_request(self) -> float:
        return self.account_proxy.get_balance()

    def handle_login(self, account_number: str) -> bool:
        account = self.account_database.login(account_number)
        if account:
            self.account_proxy = AccountProxy(account, account_number)
            self.login_status = True
            print(f"Login of {account_number} successful!")
            return True
        else:
            self.login_status = False
            print(f"Something went wrong...")
            return False

    def handle_logout(self) -> bool:
        account_number = self.account_number
        self.account_database.logout(account_number)
        self.login_status = False
        print(f"Logout successful for account {account_number}!")
        return True

    def handle_withdrawal(self, amount: float) -> bool:
        return self.account_proxy.withdraw(amount)
