from pydantic import BaseModel
from typing import List


class BankInfoModel(BaseModel):
    bank_name: str
    holder_name: str
    accounts_number: List[str]
    credit_history: List[str]


class BankInfo(BaseModel):

    def __init__(self, bank_name, holder_name, accounts_number, credit_history):
        self.bank_info_model = BankInfoModel(
            bank_name=bank_name,
            holder_name=holder_name,
            accounts_number=accounts_number,
            credit_history=credit_history
        )

    def transaction_list(self, account_number: str):
        account_numbers = []
        if account_number in self.bank_info_model.credit_history:
            account_numbers.append(account_number)
            return account_numbers
        else:
            return None
