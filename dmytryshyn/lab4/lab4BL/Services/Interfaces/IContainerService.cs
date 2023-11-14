using Lab4DataLayer.Entities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Linq.Expressions;
using System.Text;
using System.Threading.Tasks;

namespace lab4BL.Services.Interfaces
{
    public interface IContainerService
    {
        Task<IEnumerable<Container>> FilterAsync(Expression<Func<Container, bool>> filter);

        Task<IEnumerable<Container>> GetAllAsync();

        Task<Container> GetAsync(int id);

        Task InsertAsync(Container entity);

        Task Delete(Container entityToDelete);

        Task Update(Container entityToUpdate);

        Task<bool> IsExistAsync(Expression<Func<Container, bool>> filter);

        Task InsertRangeAsync(IEnumerable<Container> entity);

        Task<double> GetConsumption(int id);

        Task AddItemToContainer(int id, Item item);

    }
}
