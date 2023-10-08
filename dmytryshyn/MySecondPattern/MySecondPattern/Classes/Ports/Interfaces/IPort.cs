using MySecondPattern.Classes.Containers;
using MySecondPattern.Classes.Ships;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MySecondPattern.Classes.Ports
{
    internal interface IPort
    {
        void IncomingShip(Ship ship);
        void OutgoingShip(Ship ship);
    }
}
