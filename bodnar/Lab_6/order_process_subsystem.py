from inventory_subsystem import Stock


class ShoppingCart:
    def __init__(self, products: list[dict]):
        self.products = products

    def add_item(self, product: dict):
        self.products.append(product)

    def updated_amount(self):
        return len(self.products)

    def checkout(self, stock: Stock):
        return Order(self.products, stock)


class Order:
    def __init__(self, cart: list[dict], stock: Stock):
        self.cart = cart
        self.stock = stock

    def create_order(self):
        total_amount = self.calculate_total_amount()

        print("Order created successfully!")
        print("Total Amount: $" + str(total_amount))
        print("Items:")
        for product in self.cart:
            print("- " + product['name'])

        for product in self.cart:
            self.stock.update_stock(product['name'], 1, "remove")

    def calculate_total_amount(self):
        total_amount = 0
        for product in self.cart:
            total_amount += product.get('value', 0)

        return total_amount

    def edit_order(self, product_name: str, new_quantity: int):
        for product in self.cart:
            if product['name'] == product_name:
                old_quantity = product.get('quantity', 0)
                quantity_diff = new_quantity - old_quantity

                product['quantity'] = new_quantity

                self.stock.update_stock(product['name'], quantity_diff, "add")

                print(f"Order edited: Quantity of {product_name} updated to {new_quantity}")
                return

        print(f"Product {product_name} not found in the order. Edit failed.")
