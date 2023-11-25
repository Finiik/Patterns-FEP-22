from pydantic import BaseModel


class Stock:
    def __init__(self):
        self.stock = {}

    def select_stock_item(self, product_name: str):
        return self.stock.get(product_name, 0)

    def update_stock(self, product_name: str, price: int, action: str, quantity: int = 1):
        if action == "add":
            self.stock[product_name] = self.stock.get(product_name, {'quantity': 0, 'price': 0})
            self.stock[product_name]['quantity'] += quantity
            self.stock[product_name]['price'] = price
        elif action == "remove":
            if product_name in self.stock and self.stock[product_name]['quantity'] >= quantity:
                self.stock[product_name]['quantity'] -= quantity
            else:
                raise ValueError("Insufficient stock for removal.")
        else:
            raise ValueError("Invalid action.")

    def get_stock_status(self):
        return self.stock


class UpdateStock(BaseModel):
    product_name: str
    price: int
    action: str
    quantity: int = 1


class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def add_product(self, stock: Stock, quantity: int):
        stock.update_stock(self.name, quantity, "add")
        print(f"{quantity} {self.name}(s) added to stock.")

    def update_product(self, new_name: str = None, new_price: float = None):
        old_name = self.name
        self.name = new_name
        self.price = new_price
        if new_name is None:
            print(f"Product {self.name} updated: Price: ${new_price}")
        elif new_price is None:
            print(f"Product updated: Name from {old_name} to {new_name}")
        else:
            print(f"Product updated: Name from {old_name} to {new_name}, Price: ${new_price}")