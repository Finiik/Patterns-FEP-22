using Lab3.Builders;

namespace Lab3.Classes.Items.Abstractions
{
    abstract public class Item
    {
        public int ID { get; }
        public double Weight { get; }
        public int Count { get; }
        public int ContainerID { get; }

        public Item(int id, double weight, int count, int containerId)
        {
            ID = id;
            Weight = weight;
            Count = count;
            ContainerID = containerId;
        }

        public abstract double GetTotalWeight();
    }
}

