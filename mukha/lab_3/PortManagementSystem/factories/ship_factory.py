from ships.ship import Ship
from ships.light_weight_ship import LightWeightShip
from ships.medium_ship import MediumShip
from ships.heavy_ship import HeavyShip

class ShipFactory:
    def create_ship(self, ship_type, config):
        if ship_type == "LightWeight":
            return LightWeightShip(config)
        elif ship_type == "Medium":
            return MediumShip(config)
        elif ship_type == "Heavy":
            return HeavyShip(config)
        else:
            return Ship(config)
