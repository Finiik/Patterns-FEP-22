from dataclasses import dataclass
from BankInfo import BankInfo
from pydantic import BaseModel


@dataclass
class PersonalInfo(BaseModel):
    name: str
    client_type: str
    account_number: str
    cvv: str

    class Config:
        arbitrary_types_allowed = True


class BankCustomer(BaseModel):
    personal_info: PersonalInfo
    bank_info: BankInfo
    vip_status: bool = False
    individual_status: bool = False
    corporate_status: bool = False

    def give_details(self) -> dict:
        client_details = {
            "personal_info": {
                "name": self.personal_info.name,
                "client_type": self.personal_info.client_type,
                "account_number": self.personal_info.account_number,
                "cvv": self.personal_info.cvv
            },
            "bank_info": self.bank_info.give_details(),
            "vip_status": self.vip_status,
            "individual_status": self.individual_status,
            "corporate_status": self.corporate_status
        }
        return client_details


def VIPCustomer(cls):
    class VIPCustomerDecorator(cls):
        vip_status: bool = True

        def __init__(self, personal_info: PersonalInfo, bank_details: BankInfo):
            super().__init__(personal_info=personal_info, bank_info=bank_details, vip_status=True)

    return VIPCustomerDecorator


def IndividualCustomer(cls):
    class IndividualCustomerDecorator(cls):
        individual_status: bool = True

        def __init__(self, personal_info: PersonalInfo, bank_details: BankInfo):
            super().__init__(personal_info=personal_info, bank_info=bank_details, individual_status=True)

    return IndividualCustomerDecorator


def CorporateCustomer(cls):
    class CorporateCustomerDecorator(cls):
        corporate_status: bool = True

        def __init__(self, personal_info: PersonalInfo, bank_details: BankInfo):
            super().__init__(personal_info=personal_info, bank_info=bank_details, corporate_status=True)

    return CorporateCustomerDecorator


@VIPCustomer
class VIPCustomer(BankCustomer):
    pass


@IndividualCustomer
class IndividualCustomer(BankCustomer):
    pass


@CorporateCustomer
class CorporateCustomer(BankCustomer):
    pass
