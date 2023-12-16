from typing import List, Dict, Union
from pydantic import BaseModel


class BankInfoModel(BaseModel):
    bank_name: str
    holder_name: str
    accounts_number: List[str]
    credit_history: List[str]


class BankInfo(BaseModel):

    class Config:
        arbitrary_types_allowed = True

    def __init__(self, bank_name: str, holder_name: str, accounts_number: List[str], credit_history: List[str]):
        self.bank_info_model = BankInfoModel(
            bank_name=bank_name,
            holder_name=holder_name,
            accounts_number=accounts_number,
            credit_history=credit_history
        )

    def transaction_list(self, account_number: str) -> Union[List[str], None]:
        account_numbers = []
        if account_number in self.bank_info_model.credit_history:
            account_numbers.append(account_number)
            return account_numbers
        else:
            return None
