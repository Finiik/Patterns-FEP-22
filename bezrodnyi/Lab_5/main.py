from CreditCard import CreditCard
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from BankCustomer import BankCustomer
from BankInfo import BankInfoModel
from models import Base, BankCustomerTable, PersonalInfoTable

app = FastAPI()

engine = create_engine("sqlite:///lab5.db")
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


@app.post("/credit_cards", status_code=200)
def add_credit_card(credit_card: CreditCard, db: Session = Depends(get_db)):
    db.add(credit_card)
    db.commit()
    db.refresh(credit_card)
    return {"message": "Credit card added successfully!", "credit_card_id": credit_card.id}


@app.get("/transactions/{account_number}", status_code=200)
def show_transaction_list(account_number: str, db: Session = Depends(get_db)):
    def get_account_number_by_personal_info_id(id):
        return db.query(PersonalInfoTable).filter(PersonalInfoTable.id == id).first()

    customer = db.query(BankCustomerTable).filter(get_account_number_by_personal_info_id(
        BankCustomerTable.personal_info_id) == account_number).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")

    transactions = customer.bank_info.transaction_list(account_number)
    if transactions:
        return {"transactions": transactions}
    else:
        return {"message": "No transactions found for the account number"}
