using MySecondPattern.Classes.Containers;
using MySecondPattern.Classes.Containers.Abstractions;
using MySecondPattern.Classes.Ports;
using MySecondPattern.Classes.Ships.Characteristics;

namespace MySecondPattern.Classes.Ships
{
    internal class Ship : IShip
    {
        public int Id { get; set; }
        public double Fuel { get; set; }
        public double FuelConsumptionPerKM { get; set; }
        public Port CurrentPort { get; set; }
        public ShipLimitsCharacteristics ShipLimitsCharacteristics { get; set; }
        public List<Container> Containers { get; set; }

        public Ship(int id,
            double fuel,
            ShipLimitsCharacteristics limitsCharacteristics)
        {
            Id = id;
            Fuel = fuel;
            Containers = new List<Container>();
            ShipLimitsCharacteristics = limitsCharacteristics;
        }


        public bool Load(Container container) => Containers.Contains(container);

        public void ReFuel(double newFuel) => Fuel = newFuel;

        public bool SailTo(Port port) => CurrentPort == port;

        public bool UnLoad(Container container) => !Load(container);

        public void AddContainers(Container container)
        {
            if (!CheckCapacity(container))
            {
                Console.WriteLine("");
            }
            else
            {
                Containers.Add(container);
            }


        }

        private bool CheckCapacity(Container container)
        {
            var isUnderMaxCapacity = Containers.Count <= ShipLimitsCharacteristics.MaxNumberOfAllContainers;
            var isUnderMaxWeight = Containers.Sum(x => x.Weight) + container.Weight >= ShipLimitsCharacteristics.TotalWeightCapacity;

            var isUnderHeavyContainerCapacity =
                container is HeavyContainer
                    && Containers
                    .Where(x => x is HeavyContainer)
                    .Count() < ShipLimitsCharacteristics.MaxNumberOfHeavyContainers;

            var isUnderLiquidContainerCapacity =
                container is LiquidContainer
                    && Containers
                    .Where(x => x is LiquidContainer)
                    .Count() < ShipLimitsCharacteristics.MaxNumberOfLiquidContainers;

            var isUnderRefrigeratedContainerCapacity =
                container is RefrigeratedContainer
                         && Containers
                        .Where(x => x is RefrigeratedContainer)
                        .Count() < ShipLimitsCharacteristics.MaxNumberOfRefrigeratedContainers;

            return isUnderMaxCapacity
                && isUnderMaxWeight
                && (isUnderHeavyContainerCapacity
                || isUnderLiquidContainerCapacity
                || isUnderRefrigeratedContainerCapacity);
        }

        public void RemoveContainers(Container container) => Containers.Remove(container);
    }
}
