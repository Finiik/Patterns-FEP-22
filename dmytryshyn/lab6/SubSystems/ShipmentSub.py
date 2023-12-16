class Shipment:
    def __init__(self, shipment_type):
        self.shipment_type = shipment_type

    def define_price(self):
        return self.shipment_type.shipment_price