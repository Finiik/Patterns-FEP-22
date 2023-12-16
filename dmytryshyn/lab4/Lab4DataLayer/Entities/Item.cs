using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lab4DataLayer.Entities
{
    public class Item
    {
        public int Id { get; set; }
        public double Weight { get; set; }
        public int Count { get; set; }

        public virtual Container Container { get; set; }

    }
}
