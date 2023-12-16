using Lab4DataLayer.Entities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Linq.Expressions;
using System.Text;
using System.Threading.Tasks;

namespace lab4BL.Services.Interfaces
{
    public interface IPortService
    {
        Task<IEnumerable<Port>> FilterAsync(Expression<Func<Port, bool>> filter);

        Task<IEnumerable<Port>> GetAllAsync();

        Task<Port> GetAsync(int id);

        Task InsertAsync(Port entity);

        Task Delete(Port entityToDelete);

        Task Update(Port entityToUpdate);

        Task<bool> IsExistAsync(Expression<Func<Port, bool>> filter);

        Task InsertRangeAsync(IEnumerable<Port> entity);

        Task AddIncomingShip(Ship ship, int id);

        Task AddOutgoingShip(Ship ship, int id);

        Task<double> GetDistanceAsync(Port ship, int id);
    }
}
