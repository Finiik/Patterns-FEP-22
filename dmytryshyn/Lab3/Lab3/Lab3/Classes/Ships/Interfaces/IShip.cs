using MySecondPattern.Classes.Containers.Abstractions;
using MySecondPattern.Classes.Ports;


namespace MySecondPattern.Classes.Ships
{
    public interface IShip
    {
        bool SailTo(Port port);
        void ReFuel(double newFuel);
        bool Load(Container container);
        bool UnLoad(Container container);
    }
}
