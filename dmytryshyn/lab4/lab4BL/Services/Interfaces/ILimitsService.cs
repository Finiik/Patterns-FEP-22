using Lab4DataLayer.Entities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Linq.Expressions;
using System.Text;
using System.Threading.Tasks;

namespace lab4BL.Services.Interfaces
{
    public interface ILimitsService
    {
        Task<IEnumerable<ShipLimitsCharacteristics>> FilterAsync(Expression<Func<ShipLimitsCharacteristics, bool>> filter);

        Task<IEnumerable<ShipLimitsCharacteristics>> GetAllAsync();

        Task<ShipLimitsCharacteristics> GetAsync(int id);

        Task InsertAsync(ShipLimitsCharacteristics entity);

        Task Delete(ShipLimitsCharacteristics entityToDelete);

        Task Update(ShipLimitsCharacteristics entityToUpdate);

        Task<bool> IsExistAsync(Expression<Func<ShipLimitsCharacteristics, bool>> filter);

        Task InsertRangeAsync(IEnumerable<ShipLimitsCharacteristics> entity);
    }
}
