from fastapi import FastAPI, HTTPException, Depends
from account_db_1 import AccountDatabase
from account_proxy_1 import AccountProxy
from ATM_1 import ATMController
from customer import Customer

app = FastAPI()

account_database = AccountDatabase()

class CurrentATMController:
    def __init__(self):
        self.controller = None


current_atm_controller = CurrentATMController()


def get_current_atm_controller():
    if current_atm_controller.controller is None:
        raise HTTPException(status_code=404, detail="ATM Controller not initialized")
    return current_atm_controller.controller


@app.post("/atm/create_account/{account_number}/{amount}")
async def create_account(account_number: str, amount: float):
    global current_atm_controller
    atm_controller = ATMController(account_database, account_number, amount)
    current_atm_controller.controller = atm_controller
    account_database.create_account(account_number, amount)
    return {"message": "Account created successfully"}


@app.post("/atm/login/{account_number}")
async def atm_login(account_number: str, customer: Customer):
    global current_atm_controller
    atm_controller = ATMController(account_database, account_number, 0.0)
    current_atm_controller.controller = atm_controller

    # Attach the customer to the ATMController
    atm_controller.attach_customer(customer)

    success = atm_controller.handle_login(account_number)
    if success:
        return {"message": "ATM Login successful"}
    else:
        raise HTTPException(status_code=401, detail="ATM Login failed")


@app.post("/atm/logout")
async def atm_logout(atm_controller: ATMController = Depends(get_current_atm_controller)):
    success = atm_controller.handle_logout()
    if success:
        current_atm_controller.controller = None
        return {"message": "ATM Logout successful"}
    else:
        raise HTTPException(status_code=400, detail="ATM Logout failed")


@app.get("/atm/balance")
async def atm_balance(atm_controller: ATMController = Depends(get_current_atm_controller)):
    balance = atm_controller.handle_balance_request()
    return {"balance": balance}


@app.post("/atm/withdraw/{amount}")
async def atm_withdraw(amount: float, atm_controller: ATMController = Depends(get_current_atm_controller)):
    success = atm_controller.handle_withdrawal(amount)
    if success:
        return {"message": f"ATM Withdrawal of ${amount} successful"}
    else:
        raise HTTPException(status_code=400, detail="ATM Withdrawal failed")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
