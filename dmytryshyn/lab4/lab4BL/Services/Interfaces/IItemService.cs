using Lab4DataLayer.Entities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Linq.Expressions;
using System.Text;
using System.Threading.Tasks;

namespace lab4BL.Services.Interfaces
{
    public interface IItemService
    {
        Task<IEnumerable<Item>> FilterAsync(Expression<Func<Item, bool>> filter);

        Task<IEnumerable<Item>> GetAllAsync();

        Task<Item> GetAsync(int id);

        Task InsertAsync(Item entity);

        Task Delete(Item entityToDelete);

        Task Update(Item entityToUpdate);

        Task<bool> IsExistAsync(Expression<Func<Item, bool>> filter);

        Task InsertRangeAsync(IEnumerable<Item> entity);
    }
}
