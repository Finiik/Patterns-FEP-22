using Lab3.Builders;
using Lab3.Classes.Items.Abstractions;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lab3.Classes.Items
{
    public class Refrigerated : Item
    {
        public Refrigerated(int id, double weight, int count, int containerId) : base(id, weight, count, containerId)
        {
        }

        public override double GetTotalWeight()
        {
            return Weight * Count;
        }

        public override string ToString()
        {
            return $"Refrigerated item with ID {ID} loaded.";
        }
    }
}
