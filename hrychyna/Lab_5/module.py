from dataclasses import dataclass
import hashlib


# Decorators
def golden_credit_card(cls):
    class NewClass(cls):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.credit_limit *= 2  # Example enhancement for Golden Credit Card
    return NewClass


def corporate_credit_card(cls):
    class NewClass(cls):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.credit_limit *= 1.5  # Example enhancement for Corporate Credit Card
    return NewClass


def individual_customer(cls):
    class NewClass(cls):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.personal_info.is_individual = True
    return NewClass


def corporate_customer(cls):
    class NewClass(cls):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.personal_info.is_individual = False
    return NewClass


def vip_customer(cls):
    class NewClass(cls):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.credit_limit *= 3  # Example enhancement for VIP Customer
    return NewClass


@dataclass
class PersonalInfo:
    is_individual: bool = True


class CreditCard:
    def __init__(self, client, account_number, credit_limit, grace_period, cvv):
        self.client = client
        self.account_number = account_number
        self.credit_limit = credit_limit
        self.grace_period = grace_period
        self._cvv = cvv

    def give_details(self):
        return {
            'client': self.client,
            'account_number': self.account_number,
            'credit_limit': self.credit_limit,
            'grace_period': self.grace_period,
            'cvv': self.cvv
        }

    @property
    def cvv(self):
        return self.decrypt(self._cvv)

    @cvv.setter
    def cvv(self, value):
        self._cvv = self.encrypt(value)

    @staticmethod
    def encrypt(value):
        hashed_value = hashlib.sha256(value.encode()).hexdigest()
        return hashed_value

    def decrypt(self, value):
        input_hashed_value = hashlib.sha256(value.encode()).hexdigest()
        if input_hashed_value == self._cvv:
            return "CVV is correct"
        else:
            return "Incorrect CVV"


def transaction_list(_):
    return ["Transaction 1", "Transaction 2"]


class BankInfo:
    def __init__(self, bank_name, holder_name, accounts_number):
        self.bank_name = bank_name
        self.holder_name = holder_name
        self.accounts_number = accounts_number
        self.credit_history = {}


class BankCustomer:
    def __init__(self, personal_info, bank_details):
        self.personal_info = personal_info
        self.bank_details = bank_details

    def give_details(self):
        details = {
            'personal_info': {
                'is_individual': self.personal_info.is_individual
            },
            'bank_details': {
                'bank_name': self.bank_details.bank_name,
                'holder_name': self.bank_details.holder_name,
                'accounts_number': self.bank_details.accounts_number,
                'credit_history': self.bank_details.credit_history
            },
            'transaction_list': getattr(self.bank_details, 'transaction_list', lambda acc_num: [])(
                self.bank_details.accounts_number[0]
            )
        }
        return details
