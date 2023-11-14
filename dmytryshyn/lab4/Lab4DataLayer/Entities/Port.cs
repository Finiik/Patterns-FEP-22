using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lab4DataLayer.Entities
{
    public class Port
    {
        public int Id { get; set; }
        public double Latitude { get; set; }
        public double Longitude { get; set; }

        public virtual ICollection<Container> Containers { get; set; }
        public virtual ICollection<Ship> Ships { get; set; }


    }
}
