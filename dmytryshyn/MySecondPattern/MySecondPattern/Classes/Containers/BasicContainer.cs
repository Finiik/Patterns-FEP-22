using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using MySecondPattern.Classes.Containers.Abstractions;

namespace MySecondPattern.Classes.Containers
{
    internal class BasicContainer : Container
    {
        public double Fuel { get; set; } = 2.5;
        public BasicContainer(int id, int weight) : base(id, weight)
        {
        }

        public override double Consumption()
        {
            return Fuel * Weight;
        }
    }
}
