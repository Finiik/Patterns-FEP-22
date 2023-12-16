using MySecondPattern.Classes.Containers.Abstractions;

using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MySecondPattern.Classes.Containers
{
    public static class ContainerCreationStrategy
    {
        public static Container CreateContainer(int containerId, int weight, string type)
        {
            if (weight < 300)
            {
                return new BasicContainer(containerId, weight);
            }
            else
            {
                switch (type)
                {
                    case "R": return new RefrigeratedContainer(containerId, weight);
                    case "L": return new LiquidContainer(containerId, weight);
                    default: return new HeavyContainer(containerId, weight);
                }
            }
        }

    }
}
