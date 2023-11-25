from abc import ABC, abstractmethod
from typing import List
#import haversine as hs
from pydantic import BaseModel
from app.schemas.credit_card import *
from app.schemas.bankinfo import *
from app.schemas.personalinfo import *
from app.schemas.cryptutil import *
from cryptography.fernet import Fernet

# from app.schemas.items import Item
# from app.schemas.containers import Container

class BankCustomer(ICreditCard):
    """Implements adapter logic"""
    bank_details: BankInfo
    personal_info: str #PersonalInfo

    def decorator(funk):
        def wrapper(*args, **kwargs):
            print("wrapper starts")
            x = funk(*args, **kwargs)
            print("*args = ", args,"kwargs = ", kwargs)
            if isinstance(args, IndividualCustomer):
                x["customer_type"] = "IndividualCustomer"
            elif isinstance(args, CorporateCustomer):
                x["customer_type"] = "CorporateCustomer"
            elif isinstance(args, VIPCustomer):
                x["customer_type"] = "VIPCustomer"
            else:
                x["customer_type"] = "None"

            return x
        return wrapper

    @decorator
    def give_details(self, account_number:str) -> dict:
        trans_list = self.bank_details.transaction_list(account_number)
        a_dict: dict = {}
        a_dict["bank_name"] = self.bank_details.bank_name
        a_dict["holder_name"] = self.bank_details.holder_name
        a_dict["account_number"] = account_number
        a_dict["credit_history"] = []
        a_dict["transaction_list"] = trans_list
        return a_dict

    def encrypt(self, value: str) -> None:
        a = Cryptutil()
        self.cvv = a.encrypt(value)


    def decrypt(self, value: str) -> None:
        a = Cryptutil()
        value = a.decrypt(self.cvv)





class IndividualCustomer(BankCustomer):
    pass

class CorporateCustomer(BankCustomer):
    pass

class VIPCustomer(BankCustomer):
    pass
