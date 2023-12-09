from fastapi import FastAPI
from module import CreditCard, BankInfo, BankCustomer, PersonalInfo

app = FastAPI()

credit_card = CreditCard(client="Biosch Gerhard", account_number="4246 0123 4567 8910", credit_limit=100000.0, grace_period=30, cvv="123")
bank_info = BankInfo(bank_name="PrivatBank", holder_name="Biosch Gerhard", accounts_number=["4246 0123 4567 8910"])
bank_customer = BankCustomer(personal_info=PersonalInfo(), bank_details=bank_info)


@app.get("/credit_card_details")
def get_credit_card_details():
    return credit_card.give_details()


@app.get("/bank_customer_details")
def get_bank_customer_details():
    return bank_customer.give_details()
