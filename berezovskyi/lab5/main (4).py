from fastapi import FastAPI
from module import CreditCard, BankInfo, BankCustomer, PersonalInfo

app = FastAPI()

def create_custom_credit_card():
    return CreditCard(
        client="Alice Johnson",
        account_number="3000 4000 8000 9000",
        credit_limit=120000.0,
        grace_period=30,
        cvv="777"
    )

def create_custom_bank_customer():
    bank_info = BankInfo(
        bank_name="SuperBank",
        holder_name="Alice Johnson",
        accounts_number=["3000 4000 8000 9000"]
    )
    return BankCustomer(personal_info=PersonalInfo(), bank_details=bank_info)

credit_card = create_custom_credit_card()
bank_customer = create_custom_bank_customer()

@app.get("/credit_card_details")
def get_credit_card_details():
    return credit_card.give_details()

@app.get("/bank_customer_details")
def get_bank_customer_details():
    return bank_customer.give_details()
