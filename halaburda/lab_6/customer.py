from order_facade import BookstoreFacade


def purchase_books(books: list[dict], credit_card_number: str,
                   expiration_date: str, cvv: str, delivery_address: str, weight: float):
    bookstore_facade = BookstoreFacade()
    bookstore_facade.process_order(books, credit_card_number, expiration_date, cvv, delivery_address, weight)


class Customer:
    def __init__(self, customer_name: str):
        self.customer_name = customer_name
