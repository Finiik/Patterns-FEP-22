from abc import ABC, abstractmethod
from typing import List
#import haversine as hs
from pydantic import BaseModel

# from app.schemas.items import Item
# from app.schemas.containers import Container


class IBankInfo(BaseModel, ABC):
    """Basic abstraction"""

    @abstractmethod
    def transaction_list(self, account_number: str):
        pass


    class Config:
        orm_mode = True


class BankInfo(IBankInfo):
    """Implements port logic"""
    bank_name: str
    holder_name: str
    accounts_number: list
    credit_history:dict

    def transaction_list(self, account_number: str) -> list:
        a_list = ["0895 7643 2290 1456, 19.11.23, -200",
                  "0895 7643 2290 1456, 19.10.23, +200",
                  "0895 7643 2290 1456, 16.11.23, -2000"]

        return a_list
