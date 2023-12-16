from order_process_subs import ShoppingCart, Order
from inventory_subs import Stock
from payment_subs import Payment
from shipment_subs import Shipment


class OrderFacade:
    def __init__(self):
        self.stock = Stock()
        self.payment = Payment()
        self.shipment = Shipment()

    def doOperation(self, products: list[dict], card_number: str, expiration_date: str,
                    cvv: str, destination: str, weight: float):
        for product in products:
            self.stock.update_stock(product['name'], 1, "add")

        self.payment.add_card_details(card_number, expiration_date, cvv)

        total_amount = sum(product.get('value', 0) for product in products)
        payment_verified = self.payment.verify_payment(total_amount)

        if payment_verified:
            self.shipment.create_shipment(destination, weight)
        else:
            print("Order placement failed due to payment verification issues.")