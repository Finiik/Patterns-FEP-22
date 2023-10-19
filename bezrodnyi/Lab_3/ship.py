class Ship:
    def __init__(self, Type, weight, fuel_capacity):
        self.Type = Type
        self.weight = weight
        self.fuel_capacity = fuel_capacity
        self.items = []

    def loadItems(self, items):
        self.items.extend(items)

    def unloadItems(self):
        unloaded_items = self.items
        self.items = []
        return unloaded_items

class LightWeightShip(Ship):
    def __init__(self, Type, weight, fuel_capacity):
        super().__init__(Type, weight, fuel_capacity)
        self.ship_type = "LightWeightShip"

class MediumShip(Ship):
    def __init__(self, Type, weight, fuel_capacity):
        super().__init__(Type, weight, fuel_capacity)
        self.ship_type = "MediumShip"

class HeavyShip(Ship):
    def __init__(self, Type, weight, fuel_capacity):
        super().__init__(Type, weight, fuel_capacity)
        self.ship_type = "HeavyShip"
