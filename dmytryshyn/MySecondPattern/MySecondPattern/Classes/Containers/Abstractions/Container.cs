using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MySecondPattern.Classes.Containers.Abstractions
{
    public  abstract class Container
    {
        public int Id { get; set; }
        public int Weight { get; set; }

        public Container(int id, int weight)
        {
            Id = id;
            Weight = weight;
        }

        public abstract double Consumption();
        public bool Equals(Container other)
        {
            return Id == other.Id
                && Weight == other.Weight;
        }
    }
}
