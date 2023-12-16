from pydantic import BaseModel

class Inventory:
    def __init__(self):
        self.book_inventory = {}

    def select_book_item(self, book_title: str):
        return self.book_inventory.get(book_title, 0)

    def update_book_inventory(self, book_title: str, price: int, action: str, quantity: int = 1):
        if action == "add":
            self.book_inventory[book_title] = self.book_inventory.get(book_title, {'quantity': 0, 'price': 0})
            self.book_inventory[book_title]['quantity'] += quantity
            self.book_inventory[book_title]['price'] = price
        elif action == "remove":
            if book_title in self.book_inventory and self.book_inventory[book_title]['quantity'] >= quantity:
                self.book_inventory[book_title]['quantity'] -= quantity
            else:
                raise ValueError("Insufficient stock for removal.")
        else:
            raise ValueError("Invalid action.")

    def get_inventory_status(self):
        return self.book_inventory


class UpdateInventory(BaseModel):
    book_title: str
    price: int
    action: str
    quantity: int = 1


class Book:
    def __init__(self, title: str, price: float):
        self.title = title
        self.price = price

    def add_book(self, inventory: Inventory, quantity: int):
        inventory.update_book_inventory(self.title, quantity, "add")
        print(f"{quantity} copies of '{self.title}' added to the inventory.")

    def update_book(self, new_title: str = None, new_price: float = None):
        old_title = self.title
        self.title = new_title
        self.price = new_price
        if new_title is None:
            print(f"Book '{self.title}' updated: Price: ${new_price}")
        elif new_price is None:
            print(f"Book updated: Title from '{old_title}' to '{new_title}'")
        else:
            print(f"Book updated: Title from '{old_title}' to '{new_title}', Price: ${new_price}")

# No changes to the other code in inventory_subs.py
