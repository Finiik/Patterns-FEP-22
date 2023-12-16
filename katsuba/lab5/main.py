from fastapi import FastAPI
from module import CreditCard, BankInfo, BankCustomer, PersonalInfo

app = FastAPI()

credit_card = CreditCard(client="Donald Petrenko", account_number="1000 2000 4000 5000", credit_limit=100000.0, grace_period=25, cvv="666")
bank_info = BankInfo(bank_name="MonoBank", holder_name="Donald Petrenko", accounts_number=["1000 2000 4000 5000"])
bank_customer = BankCustomer(personal_info=PersonalInfo(), bank_details=bank_info)


@app.get("/credit_card_details")
def get_credit_card_details():
    return credit_card.give_details()


@app.get("/bank_customer_details")
def get_bank_customer_details():
    return bank_customer.give_details()
