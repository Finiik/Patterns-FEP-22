from ship import LightWeightShip, MediumShip, HeavyShip
from item import Small, Heavy, Refrigerated, Liquid

class ItemFactory:
    @staticmethod
    def createSmallItem(ID, weight, count, containerID):
        return Small(ID, weight, count, containerID)

    @staticmethod
    def createHeavyItem(ID, weight, count, containerID):
        return Heavy(ID, weight, count, containerID)

    @staticmethod
    def createRefrigeratedItem(ID, weight, count, containerID):
        return Refrigerated(ID, weight, count, containerID)

    @staticmethod
    def createLiquidItem(ID, weight, count, containerID):
        return Liquid(ID, weight, count, containerID)

class ShipFactory:
    @staticmethod
    def createLightWeightShip(Type, weight, fuel_capacity):
        return LightWeightShip(Type, weight, fuel_capacity)

    @staticmethod
    def createMediumShip(Type, weight, fuel_capacity):
        return MediumShip(Type, weight, fuel_capacity)

    @staticmethod
    def createHeavyShip(Type, weight, fuel_capacity):
        return HeavyShip(Type, weight, fuel_capacity)
