using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MySecondPattern.Classes.Containers
{
    internal class LiquidContainer : HeavyContainer
    {
        public new double Fuel { get; set; } = 4.0;
        public LiquidContainer(int id, int weight) : base(id, weight)
        {
        }
    }
}
