
using MySecondPattern.Classes.Containers.Abstractions;
using MySecondPattern.Classes.Ships;

namespace MySecondPattern.Classes.Ports
{
    public class Port : IPort
    {
        public int Id { get; set; }
        public double Latitude { get; set; }
        public double Longitude { get; set; }
        public List<Container> Containers { get; set; } = new List<Container>();
        public List<Ship> History { get; set; } = new List<Ship>();
        public List<Ship> Current { get; set; } = new List<Ship>();

        public Port(int id, double latitude, double longitude)
        {
            Id = id;
            Latitude = latitude;
            Longitude = longitude;
        }
        public void IncomingShip(Ship ship) => Current.Add(ship);

        public void OutgoingShip(Ship ship)
        {
            Current.Remove(ship);
            History.Add(ship);
        }

        public double GetDistance(Port other)
        {
            var radiusOfEarth = 6371;

            var diffLatitude = Math.PI * (other.Latitude - Latitude) / 180;
            var diffLongitude = Math.PI * (other.Longitude - Longitude) / 180;

            var Unknown = Math.Pow(Math.Sin(diffLatitude * 2), 2)
                + Math.Cos(Math.PI * Latitude / 180)
                * Math.Cos(Math.PI * other.Latitude / 180)
                * Math.Pow(Math.Sin(diffLongitude / 2), 2);
            return radiusOfEarth * Unknown;
        }
    }
}
