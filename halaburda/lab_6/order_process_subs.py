# order_process_subs.py (Bookstore Order Process)
from inventory_subs import Inventory  # Updated import statement


class BookShoppingCart:
    def __init__(self, books: list[dict]):
        self.books = books

    def add_book(self, book: dict):
        self.books.append(book)

    def updated_amount(self):
        return len(self.books)

    def checkout(self, inventory: Inventory):
        return BookOrder(self.books, inventory)


class BookOrder:
    def __init__(self, cart: list[dict], inventory: Inventory):
        self.cart = cart
        self.inventory = inventory

    def create_order(self):
        total_amount = self.calculate_total_amount()

        print("Order created successfully!")
        print("Total Amount: $" + str(total_amount))
        print("Books:")
        for book in self.cart:
            print("- " + book['title'])

        for book in self.cart:
            self.inventory.update_book_inventory(book['title'], 1, "remove")

    def calculate_total_amount(self):
        total_amount = 0
        for book in self.cart:
            total_amount += book.get('price', 0)

        return total_amount

    def edit_order(self, book_title: str, new_quantity: int):
        for book in self.cart:
            if book['title'] == book_title:
                old_quantity = book.get('quantity', 0)
                quantity_diff = new_quantity - old_quantity

                book['quantity'] = new_quantity

                self.inventory.update_book_inventory(book['title'], quantity_diff, "add")

                print(f"Order edited: Quantity of '{book_title}' updated to {new_quantity}")
                return

        print(f"Book '{book_title}' not found in the order. Edit failed.")

# No changes to the other code in order_process_subs.py
