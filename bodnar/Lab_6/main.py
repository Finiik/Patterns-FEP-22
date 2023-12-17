from fastapi import FastAPI, Depends, Body
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Base, StockTable, Order
from order_facade import OrderFacade
from inventory_subsystem import Stock, UpdateStock

app = FastAPI()

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)


def get_db():
    db = Session(engine)
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
    stock_instance = Stock()
    stock_instance.update_stock(stock.product_name, stock.price, stock.action, stock.quantity)
    new_item = StockTable(product_name=stock.product_name, price=stock.price, quantity=stock.quantity)
    db.add(new_item)
    db.commit()
    return item_in_stock


def execute_do_operation(products: list[dict], card_number: str, expiration_date: str,
                         cvv: str, destination: str, db: Session = Depends(get_db)):
    order_facade = OrderFacade()

    new_order = Order(card_number=card_number, expiration_date=expiration_date, cvv=cvv,
                      destination=destination)
    db.add(new_order)
    db.commit()

    order_facade.do_operation(products, card_number, expiration_date, cvv, destination)


@app.post("/execute_do_operation")
def execute_do_operation_endpoint(
    card_number: str,
    expiration_date: str,
    cvv: str,
    destination: str,
    products: list[dict] = Body(...),
    db: Session = Depends(get_db)
):
    execute_do_operation(products, card_number, expiration_date, cvv, destination, db)
    return {"message": "do_operation executed successfully!"}
