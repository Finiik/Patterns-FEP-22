from inventory_subsystem import Stock
from payment_subsystem import Payment
from shipment_subsystem import Shipment


class OrderFacade:
    def __init__(self):
        self.stock = Stock()
        self.payment = Payment()
        self.shipment = Shipment()

    def do_operation(self,
                     products: list[dict],
                     card_number: str,
                     expiration_date: str,
                     cvv: str,
                     destination: str
                     ):
        for product in products:
            self.stock.update_stock(product['name'], 1, "add")

        self.payment.add_card_details(card_number, expiration_date, cvv)

        total_amount = sum(product.get('value', 0) for product in products)
        payment_verified = self.payment.verify_payment(total_amount)

        if payment_verified:
            self.shipment.create_shipment(destination)
        else:
            print("Order placement failed due to payment verification issues.")
