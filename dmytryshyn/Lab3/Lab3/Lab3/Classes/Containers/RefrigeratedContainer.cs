using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MySecondPattern.Classes.Containers
{
    public class RefrigeratedContainer : HeavyContainer
    {
        public new double Fuel { get; set; } = 5.0;
        public RefrigeratedContainer(int id, int weight) : base(id, weight)
        {
        }
    }
}
