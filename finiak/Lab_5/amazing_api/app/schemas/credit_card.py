from abc import ABC, abstractmethod
from typing import List
#import haversine as hs
from pydantic import BaseModel
from app.schemas.cryptutil import *

# from app.schemas.items import Item
# from app.schemas.containers import Container


class ICreditCard(BaseModel, ABC):
    """Basic abstraction"""

    #id: int

    @abstractmethod
    def give_details(self):
        pass

    @abstractmethod
    def encrypt(self, value: str):
        pass

    @abstractmethod
    def decrypt(self, value: str):
        pass

    class Config:
        orm_mode = True


class CreditCard(ICreditCard):
    """Implements port logic"""

    client: str
    account_number: str
    credit_limit: float
    grace_period: int
    cvv: str

    def give_details(self) -> dict:
        cvv = "657"
        cvv02 = ""
        self.encrypt(cvv)
        self.decrypt(cvv02)
        a_dict: dict = {}
        a_dict["account_number"] = self.account_number
        a_dict["cvv.codet"] = self.cvv
        a_dict["cvv"] = cvv02
        return a_dict

    def encrypt(self, value: str) -> None:
        a = Cryptutil()
        self.cvv = a.encrypt(value)


    def decrypt(self, value: str) -> None:
        a = Cryptutil()
        value = a.decrypt(self.cvv)