from dataclasses import dataclass
import hashlib
from collections import defaultdict


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
            'cvv': self.decrypt(self._cvv)
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


def apply_credit_card_decorator(cls, multiplier):
    class NewClass(cls):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.credit_limit *= multiplier

    return NewClass


def apply_customer_decorator(cls, is_individual):
    class NewClass(cls):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.personal_info.is_individual = is_individual

    return NewClass


golden_credit_card = apply_credit_card_decorator(CreditCard, 2)
corporate_credit_card = apply_credit_card_decorator(CreditCard, 1.5)


class BankCustomer:
    pass


individual_customer = apply_customer_decorator(BankCustomer, True)
corporate_customer = apply_customer_decorator(BankCustomer, False)
vip_customer = apply_credit_card_decorator(BankCustomer, 3)


@dataclass
class BankInfo:
    bank_name: str
    holder_name: str
    accounts_number: list
    credit_history: defaultdict = None

    def __post_init__(self):
        if self.credit_history is None:
            self.credit_history = defaultdict(list)


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
