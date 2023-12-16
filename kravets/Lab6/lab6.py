
class OrderFacade:
    def __init__(self):
        self.shopping_cart = ShoppingCart()
        self.order = Order()
        self.stock = Stock()
        self.product = Product()
        self.shipment = Shipment()
        self.shipment_provider = ShipmentProvider()
        self.payment = Payment()

    def doOperation(self):
        self.shopping_cart.addItem()
        self.shopping_cart.updateAmount()
        self.shopping_cart.checkout()

        self.order.createOrder()
        self.order.editOrder()

        self.stock.selectStockItem()
        self.stock.updateStock()

        self.product.addProduct()
        self.product.updateProduct()

        self.shipment.createShipment()
        self.shipment.addProvider()

        self.shipment_provider.addProvider()
        self.shipment_provider.modifyProvider()

        self.payment.addCardDetails()
        self.payment.verifyPayment()

class ShoppingCart:
    def addItem(self):
        print("Adding to the basket")

    def updateAmount(self):
        print("Updating amount of goods in busket")

    def checkout(self):
        print("Make purchuse")

class Order:
    def createOrder(self):
        print("Make an order")

    def editOrder(self):
        print("Edit an order")

class Stock:
    def selectStockItem(self):
        print("Chosing an item from the storage")

    def updateStock(self):
        print("Update order")

class Product:
    def addProduct(self):
        print("Add item")

    def updateProduct(self):
        print("Updating item")

class Shipment:
    def createShipment(self):
        print("Make shipping")

    def addProvider(self):
        print("Add shipper")

class ShipmentProvider:
    def addProvider(self):
        print("Add shipper")

    def modifyProvider(self):
        print("Change shipper")

class Payment:
    def addCardDetails(self):
        print("Adding card data")

    def verifyPayment(self):
        print("Payment check")

if __name__ == "__main__":
    facade = OrderFacade()
    facade.doOperation()
