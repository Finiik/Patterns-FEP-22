# order_facade.py (Bookstore Order Facade)
class ShoppingCart:
    pass


class Order:
    pass


from inventory_subs import Inventory  # Updated import statement
from payment_subs import Payment  # Updated import statement
from shipment_subs import Shipment  # Updated import statement


class BookstoreFacade:
    def __init__(self):
        self.inventory = Inventory()  # Updated class instantiation
        self.payment = Payment()  # Updated class instantiation
        self.shipment = Shipment()  # Updated class instantiation

    def process_order(self, books: list[dict], credit_card_number: str, expiration_date: str,
                      cvv: str, delivery_address: str, weight: float):
        for book in books:
            self.inventory.update_book_inventory(book['title'], 1, "add")

        self.payment.add_card_details(credit_card_number, expiration_date, cvv)

        total_amount = sum(book.get('price', 0) for book in books)
        payment_verified = self.payment.verify_payment(total_amount)

        if payment_verified:
            self.shipment.create_shipment(delivery_address, weight)
        else:
            print("Order placement failed due to payment verification issues.")

# No changes to the other code in order_facade.py
