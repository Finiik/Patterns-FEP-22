from account_proxy import AccountProxy
from account import Account


def make_account_proxy(start_amount):
    return AccountProxy(start_amount)


class DatabaseProxy:
    def __init__(self):
        self.the_real_account = None

    def login(self, account_number, amount):
        self.the_real_account = self.login(account_number)
        balance = Account.get_balance(amount)
        return make_account_proxy(balance)

    def logout(self, account_proxy):
        if account_proxy in self.the_real_account.logged_in_accounts:
            self.the_real_account.set_balance(account_proxy.get_balance())
            self.the_real_account.logged_in_accounts.remove(account_proxy)
            print("Logout successful.")
        else:
            print("Account not found in logged-in accounts.")
