using Lab3.Enums;
using MySecondPattern.Classes.Ships.Characteristics;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lab3.DTO
{
    public class ShipDTO
    {
        public int Id { get; set; }
        public double Fuel { get; set; }
        public ShipLimitsCharacteristics ShipLimitsCharacteristics { get; set; }
        public ShipTypes ShipTypes { get; set; }
    }
}
