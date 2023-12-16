using Lab4DataLayer.Entities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Linq.Expressions;
using System.Text;
using System.Threading.Tasks;

namespace lab4BL.Services.Interfaces
{
    public interface IShipService
    {
        Task<IEnumerable<Ship>> FilterAsync(Expression<Func<Ship, bool>> filter);

        Task<IEnumerable<Ship>> GetAllAsync();

        Task<Ship> GetAsync(int id);

        Task InsertAsync(Ship entity);

        Task Delete(Ship entityToDelete);

        Task Update(Ship entityToUpdate);

        Task<bool> IsExistAsync(Expression<Func<Ship, bool>> filter);

        Task InsertRangeAsync(IEnumerable<Ship> entity);

        Task<bool> SailTo(Port port, int id);

        Task ReFuel(double newFuel, int id);

        Task<bool> Load(int shipId, int containerId);

        Task<bool> UnLoad(int shipId, int containerId);
        Task AddContainers(Container container, int id);
        Task RemoveContainers(int shipId, int containerId);
    }
}
