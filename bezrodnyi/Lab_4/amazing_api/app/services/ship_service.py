from app.schemas.ship import LightWeightShip, MediumWeightShip, HeavyWeightShip


class ShipCreator:

    @staticmethod
    def create_ship(ship_config):
        total_weight_capacity = ship_config.get('total_weight_capacity')

        if 1 <= total_weight_capacity <= 40_000:
            return LightWeightShip(**ship_config)
        elif 40_000 < total_weight_capacity <= 70_000:
            return MediumWeightShip(**ship_config)
        elif total_weight_capacity >= 70_000:
            return HeavyWeightShip(**ship_config)
        else:
            raise ValueError(f"Invalid ship total weight capacity: {total_weight_capacity}")
