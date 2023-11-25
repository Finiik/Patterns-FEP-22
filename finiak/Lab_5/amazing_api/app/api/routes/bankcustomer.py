from fastapi import APIRouter, Depends
from fastapi import HTTPException
from starlette import status
from app.schemas.bankcustomer import *
from app.schemas.bankinfo import *
from app.schemas.credit_card import *
from app.db.database import get_db


from sqlalchemy.orm import Session

router = APIRouter()

""" 
@router.get("/update", status_code=status.HTTP_201_CREATED)
def update_port( db: Session = Depends(get_db)):
    port_crud = PortRepository(db_session=db)
    db_port = port_crud.get_by_id(port_id=1)
    if db_port:
        db_port = port_crud.update_port(port=db_port)
    else:
        raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Port does not exist"
    )
    return db_port
"""




@router.get("/", response_model=dict, status_code=status.HTTP_200_OK)
def get_bank_customer():
    print(f"===== get_bank_customer =======")
    bank_info = BankInfo(bank_name= "Privat", holder_name = "State",
                         accounts_number=[], credit_history={})
    credit_card = VIPCustomer(bank_details=bank_info, personal_info="Some personal info")
    return credit_card.give_details("0895 7643 2290 1456")

@router.get("/cvv", response_model=dict, status_code=status.HTTP_200_OK)
def get_cvv():
    print(f"===== get_cvv =======")
    credit_card = CreditCard(client= "Katya", account_number= "0895 7643 2290 1456",
                             credit_limit= "8000.0", grace_period= "6", cvv= "")
    return credit_card.give_details()
