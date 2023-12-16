using Lab3.Classes.Ships.Implementations;
using Lab3.Enums;
using MySecondPattern.Classes.Ports;
using MySecondPattern.Classes.Ships;
using MySecondPattern.Classes.Ships.Characteristics;


namespace Lab3.Classes.Ships
{
    public static class ShipFactory
    {
        public static Ship CreateShip(ShipTypes shipType, int shipId, ShipLimitsCharacteristics shipConfig, double fuel)
        {
            switch (shipType)
            {
                case ShipTypes.LightWeightShip:
                    return new LightWeightShip(shipId, fuel, shipConfig);
                case ShipTypes.MediumShip:
                    return new MediumShip(shipId, fuel, shipConfig);
                case ShipTypes.HeavyShip:
                    return new HeavyShip(shipId, fuel, shipConfig);
                default:
                    throw new ArgumentException($"Invalid item type: {shipType}");
            }
        }
    }
}
