from order_facade import OrderFacade


class Customer:
    def __init__(self, name: str):
        self.name = name

    def order_item(self, products: list[dict], card_number: str,
                   expiration_date: str, cvv: str, destination: str, weight: float):
        facade = OrderFacade()
        facade.doOperation(products, card_number, expiration_date, cvv, destination, weight)