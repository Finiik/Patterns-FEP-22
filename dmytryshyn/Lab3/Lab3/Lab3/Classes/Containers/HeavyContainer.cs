using MySecondPattern.Classes.Containers.Abstractions;

namespace MySecondPattern.Classes.Containers
{
    public class HeavyContainer : Container
    {
        public double Fuel { get; set; } = 2.5;
        public HeavyContainer(int id, int weight) : base(id, weight)
        {
        }

        public override double Consumption()
        {
            return Fuel * Weight;
        }
    }
}
