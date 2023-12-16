using Lab3.Classes.Items;
using Lab3.Classes.Items.Abstractions;

namespace Lab3.Builders
{
    public static class ItemBuilder
    {
        public static Item CreateItem(string itemType, int id, double weight, int count, int containerId)
        {
            switch (itemType)
            {
                case "Small":
                    return new Small(id,  weight,  count,  containerId);
                case "Heavy":
                    return new Heavy(id, weight, count, containerId);
                case "Refrigerated":
                    return new Refrigerated(id, weight, count, containerId);
                case "Liquid":
                    return new Liquid(id, weight, count, containerId);
                default:
                    throw new ArgumentException($"Invalid item type: {itemType}");
            }
        }
    }
}
