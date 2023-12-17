# main.py (FastAPI application)
from fastapi import FastAPI, Depends, HTTPException, Body
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Base, Stock, Order  # Assuming you have a Product model
from order_facade import OrderFacade  # Assuming you have an OrderFacade class
from inventory_subs import Stock, UpdateStock  # Assuming you have a Stock class

app = FastAPI()

engine = create_engine("sqlite:///./test.db")
Base.metadata.create_all(bind=engine)


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()


@app.post("/update_stock")
def update_stock_with_products(stock: UpdateStock, db: Session = Depends(get_db)):
    item_in_stock = {
        "product_name": stock.product_name,
        "price": stock.price,
        "action": stock.action,
        "quantity": stock.quantity
    }
    stock.update_stock(stock.product_name, stock.price, stock.action, stock.quantity)
    new_item = Stock(product_name=stock.product_name, price=stock.price, quantity=stock.quantity)
    db.add(new_item)
    db.commit()
    return item_in_stock


def execute_do_operation(card_number: str, expiration_date: str,
                         cvv: str, destination: str, weight: float, products: list[dict], db: Session = Depends(get_db)):
    order_facade = OrderFacade()

    new_order = Order(card_number=card_number, expiration_date=expiration_date, cvv=cvv,
                      destination=destination, weight=weight)
    db.add(new_order)
    db.commit()

    order_facade.doOperation(products, card_number, expiration_date, cvv, destination, weight)


@app.post("/execute_do_operation")
def execute_do_operation_endpoint(
    card_number: str, expiration_date: str, cvv: str, destination: str, weight: float, products: list[dict] = Body(...), db: Session = Depends(get_db)
):
    execute_do_operation(card_number, expiration_date, cvv, destination, weight, products, db)
    return {"message": "doOperation executed successfully!"}
