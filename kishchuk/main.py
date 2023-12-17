from credit_card import CreditCard
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from bank_customer import BankCustomer
from bank_info import BankInfoModel
from models import Base, BankCustomerTable

app = FastAPI()

engine = create_engine("sqlite:///./test.db")
Base.metadata.create_all(bind=engine)


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()


@app.post("/customers/", response_model=BankInfoModel, status_code=200)
def add_customer(customer: BankCustomer, db: Session = Depends(get_db)):
    db.add(customer)
    db.commit()
    db.refresh(customer)
    return {"message": "Customer added successfully!", "customer": customer}


# Add a credit card
@app.post("/creditcards/", status_code=200)
def add_credit_card(credit_card: CreditCard, db: Session = Depends(get_db)):
    db.add(credit_card)
    db.commit()
    db.refresh(credit_card)
    return {"message": "Credit card added successfully!", "credit_card_id": credit_card.id}


@app.get("/transactions/{account_number}", status_code=200)
def show_transaction_list(account_number: str, db: Session = Depends(get_db)):
    customer = db.query(BankCustomerTable).filter(BankCustomerTable.personal_info.account_number == account_number).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")

    transactions = customer.bank_info.transaction_list(account_number)
    if transactions:
        return {"transactions": transactions}
    else:
        return {"message": "No transactions found for the account number"}

