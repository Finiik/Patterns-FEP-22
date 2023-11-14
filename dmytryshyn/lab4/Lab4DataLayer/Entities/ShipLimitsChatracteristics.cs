using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lab4DataLayer.Entities
{
    public class ShipLimitsCharacteristics
    {
        public int Id { get; set; }
        public int TotalWeightCapacity { get; set; }
        public int MaxNumberOfAllContainers { get; set; }
        public int MaxNumberOfHeavyContainers { get; set; }
        public int MaxNumberOfRefrigeratedContainers { get; set; }
        public int MaxNumberOfLiquidContainers { get; set; }
    }
}
