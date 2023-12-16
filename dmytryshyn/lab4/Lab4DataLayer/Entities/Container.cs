using Lab4DataLayer.Enums;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lab4DataLayer.Entities
{
    public class Container
    {
        public int Id { get; set; }
        public int Weight { get; set; }
        public double Fuel { get; set; }
        public ContainerTypes ContainerType { get; set; }
        public int? PortId { get; set; }
        public int? ShipId { get; set; }

        public virtual ICollection<Item> Items { get; set; }

    }
}
