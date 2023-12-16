from DB import TableCard, TableProvider, TableProducts, engine, session
from CustomerOperation.OrderFacade import OrderFacade
from SubSystems.ShipmentSub import Shipment
from SubSystems.PaymentSub import Payment
from SubSystems.InventorySub import Stock
from SubSystems.OrderingSub import Order
from Models import CustomerModel
from fastapi import FastAPI, HTTPException

app = FastAPI()


connection = engine.connect()


@app.post('/PostOrder')
def make_order(customer_data: CustomerModel):
    """Shipment types:
        'Nova poshta' for fastest delivery
        'Ukr poshta' for cheapest delivery
        'Meest' for normal delivery
    """
    product_data = session.query(TableProducts).filter(TableProducts.product_name == customer_data.item).first()
    provider_data = session.query(TableProvider).filter(TableProvider.name == customer_data.shipment_type).first()
    card_data = session.query(TableCard).filter(TableCard.card_number == customer_data.card_number).first()
    if not product_data or not provider_data or not card_data:
        raise HTTPException(status_code=400, detail='Invalid input, try again')
    stock = Stock(customer_data.item, customer_data.amount, product_data.amount)
    shipment = Shipment(provider_data)
    order = Order(customer_data.item, customer_data.amount, product_data.price, shipment.define_price())
    payment = Payment(card_data.balance, order.total_price())
    facade = OrderFacade(order, stock, shipment, payment)
    status, message = facade.request()
    if status is False:
        raise HTTPException(status_code=400, detail=f'{message}')
    else:
        product_data.amount = stock.check_stock()
        card_data.balance = payment.update_balance()
        session.commit()
        return message