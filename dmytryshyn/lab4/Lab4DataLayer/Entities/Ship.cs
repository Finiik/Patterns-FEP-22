using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lab4DataLayer.Entities
{
    public class Ship
    {
        public int Id { get; set; }
        public double Fuel { get; set; }
        public double FuelConsumptionPerKM { get; set; }

        public virtual ShipLimitsCharacteristics Characteristics { get; set; }
        public virtual Port Port { get; set; }
        public virtual ICollection<Container> Containers { get; set; }
    }
}
