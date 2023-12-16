# Запит
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
        # Виконання послідовності операцій для оформлення замовлення
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

# Підсистема процесу замовлення
class ShoppingCart:
    def addItem(self):
        print("Додавання товару до кошика")

    def updateAmount(self):
        print("Оновлення кількості товарів у кошику")

    def checkout(self):
        print("Оформлення покупок")

class Order:
    def createOrder(self):
        print("Створення замовлення")

    def editOrder(self):
        print("Редагування замовлення")

# Підсистема інвентаризації
class Stock:
    def selectStockItem(self):
        print("Вибір товару на складі")

    def updateStock(self):
        print("Оновлення запасів")

class Product:
    def addProduct(self):
        print("Додавання товару")

    def updateProduct(self):
        print("Оновлення товару")

# Система доставки
class Shipment:
    def createShipment(self):
        print("Створення відправлення")

    def addProvider(self):
        print("Додавання постачальника доставки")

class ShipmentProvider:
    def addProvider(self):
        print("Додавання постачальника доставки")

    def modifyProvider(self):
        print("Зміна постачальника доставки")

# Підсистема оплати
class Payment:
    def addCardDetails(self):
        print("Додавання даних карти")

    def verifyPayment(self):
        print("Перевірка оплати")

# Приклад використання Facade
if __name__ == "__main__":
    facade = OrderFacade()
    facade.doOperation()
