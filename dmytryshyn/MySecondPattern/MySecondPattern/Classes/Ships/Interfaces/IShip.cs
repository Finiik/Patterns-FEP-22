using MySecondPattern.Classes.Containers;
using MySecondPattern.Classes.Containers.Abstractions;
using MySecondPattern.Classes.Ports;


namespace MySecondPattern.Classes.Ships
{
    internal interface IShip
    {
        bool SailTo(Port port);
        void ReFuel(double newFuel);
        bool Load(Container container);
        bool UnLoad(Container container);

    }
}
