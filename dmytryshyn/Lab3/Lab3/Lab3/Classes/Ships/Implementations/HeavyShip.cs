using MySecondPattern.Classes.Ships;
using MySecondPattern.Classes.Ships.Characteristics;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lab3.Classes.Ships.Implementations
{
    public class HeavyShip : Ship
    {
        public HeavyShip(int id, double fuel, ShipLimitsCharacteristics limitsCharacteristics) : base(id, fuel, limitsCharacteristics)
        {
        }
        public override string ToString()
        {
            return $"The ship {Id} is a heavy ship.";
        }
    }
}
