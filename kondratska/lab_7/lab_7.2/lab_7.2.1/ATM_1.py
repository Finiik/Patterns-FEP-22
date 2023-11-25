from account_proxy_1 import AccountProxy
from account_db_1 import AccountDatabase
from customer import Customer


class ATMController:
    def __init__(self, account_database: AccountDatabase, account_number: str, amount: float):
        self.account_proxy = AccountProxy(account_database.login(account_number), account_number)
        self.account_database = account_database
        self.account_number = account_number
        self.amount = amount
        self.login_status = False
        self.attached_customers = []  # Maintain a list of attached customers

    def attach_customer(self, customer: Customer) -> None:
        if customer not in self.attached_customers:
            self.attached_customers.append(customer)
            customer.attach_customer(self.account_proxy)

    def detach_customer(self, customer: Customer) -> None:
        if customer in self.attached_customers:
            self.attached_customers.remove(customer)
            customer.detach_customer(self.account_proxy)

    def notify_customers(self) -> None:
        for customer in self.attached_customers:
            customer.notify(self.account_proxy)

    def handle_balance_request(self) -> float:
        return self.account_proxy.get_balance()

    def handle_login(self, account_number: str) -> bool:
        account = self.account_database.login(account_number)
        if account:
            self.account_proxy = AccountProxy(account, account_number)
            self.login_status = True
            print(f"Login of {account_number} successful!")
            self.notify_customers()  # Notify customers on login
            return True
        else:
            self.login_status = False
            print(f"Something went wrong...")
            return False

    def handle_logout(self) -> bool:
        account_number = self.account_number
        self.account_database.logout(account_number)
        self.login_status = False
        self.notify_customers()
        print(f"Logout successful for account {account_number}!")
        return True

    def handle_withdrawal(self, amount: float) -> bool:
        success = self.account_proxy.withdraw(amount)
        if success:
            self.notify_customers()
        return success
