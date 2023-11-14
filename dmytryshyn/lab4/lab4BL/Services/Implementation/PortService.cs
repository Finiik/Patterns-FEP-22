using lab4BL.Services.Interfaces;
using Lab4DataLayer.Entities;
using Lab4DataLayer.Repositories;
using System.Linq.Expressions;

namespace lab4BL.Services.Implementation
{
    public class PortService : IPortService
    {
        private readonly IRepository<Port> _portRepository;

        public PortService(IRepository<Port> itemRepository)
        {
            _portRepository = itemRepository;
        }

        public async Task AddIncomingShip(Ship ship, int id)
        {
            var port = await _portRepository.GetAsync(id);
            if (port != null) 
            {
                return;
            }

            port.Ships.Add(ship);
            await Update(port);
        }

        public async Task AddOutgoingShip(Ship ship, int id)
        {
            var port = await _portRepository.GetAsync(id);
            if (port != null)
            {
                return;
            }
            port.Ships.Remove(ship);
            await Update(port);
        }

        public async Task Delete(Port entityToDelete)
        {
            _portRepository.Delete(entityToDelete);
            await _portRepository.SaveChanges();
        }

        public async Task<IEnumerable<Port>> FilterAsync(Expression<Func<Port, bool>> filter)
        {
            return await _portRepository.FilterAsync(filter);
        }

        public async Task<IEnumerable<Port>> GetAllAsync()
        {
            return await _portRepository.GetAllAsync();
        }

        public async Task<Port> GetAsync(int id)
        {
            return await _portRepository.GetAsync(id);
        }

        public async Task<double> GetDistanceAsync(Port ship, int id)
        {
            var port = await _portRepository.GetAsync(id);
            if (port != null)
            {
                return 0;
            }

            var radiusOfEarth = 6371;

            var diffLatitude = Math.PI * (ship.Latitude - port.Latitude) / 180;
            var diffLongitude = Math.PI * (ship.Longitude - port.Longitude) / 180;

            var Unknown = Math.Pow(Math.Sin(diffLatitude * 2), 2)
                + Math.Cos(Math.PI * port.Latitude / 180)
                * Math.Cos(Math.PI * ship.Latitude / 180)
                * Math.Pow(Math.Sin(diffLongitude / 2), 2);
            return radiusOfEarth * Unknown;
        }

        public async Task InsertAsync(Port entity)
        {
            await _portRepository.InsertAsync(entity);
        }

        public async Task InsertRangeAsync(IEnumerable<Port> entity)
        {
            await _portRepository.InsertRangeAsync(entity);
            await _portRepository.SaveChanges();
        }

        public async Task<bool> IsExistAsync(Expression<Func<Port, bool>> filter)
        {
            return await _portRepository.IsExistAsync(filter);
        }

        public async Task Update(Port entityToUpdate)
        {
            _portRepository.Update(entityToUpdate);
            await _portRepository.SaveChanges();
        }
    }
}
