from SubSystems.OrderingSub import Order
from SubSystems.InventorySub import Stock
from SubSystems.ShipmentSub import Shipment
from SubSystems.PaymentSub import Payment


class OrderFacade:
    def __init__(self, order: Order, stock: Stock, shipment: Shipment, payment: Payment):
        self.order = order
        self.stock = stock
        self.shipment = shipment
        self.payment = payment

    def request(self):
        new_stock = self.stock.check_stock()
        if new_stock is None:
            return False, 'Item is absent, transaction declined'
        verify_payment = self.payment.verify_payment()
        if verify_payment is not False:
            return True, f'Payment was made successfull, new balance: {self.payment.update_balance()}'
        else:
            return False, 'Payment cannot be done: balance is too small'