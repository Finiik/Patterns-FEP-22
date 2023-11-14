

using lab4BL.Services.Interfaces;
using Lab4DataLayer.Entities;
using Lab4DataLayer.Enums;
using Lab4DataLayer.Repositories;
using System.Linq.Expressions;

namespace lab4BL.Services.Implementation
{
    public class LimitsService : ILimitsService
    {
        private readonly IRepository<ShipLimitsCharacteristics> _shipLimitsCharacteristics;

        public LimitsService(IRepository<ShipLimitsCharacteristics> shipLimitsCharacteristics)
        {
            _shipLimitsCharacteristics = shipLimitsCharacteristics;
        }
        public async Task Delete(ShipLimitsCharacteristics entityToDelete)
        {
            _shipLimitsCharacteristics.Delete(entityToDelete);
            await _shipLimitsCharacteristics.SaveChanges();
        }

        public async Task<IEnumerable<ShipLimitsCharacteristics>> FilterAsync(Expression<Func<ShipLimitsCharacteristics, bool>> filter)
        {
            return await _shipLimitsCharacteristics.FilterAsync(filter);
        }

        public async Task<IEnumerable<ShipLimitsCharacteristics>> GetAllAsync()
        {
            return await _shipLimitsCharacteristics.GetAllAsync();
        }

        public async Task<ShipLimitsCharacteristics> GetAsync(int id)
        {
            return await _shipLimitsCharacteristics.GetAsync(id);
        }

        public async Task InsertAsync(ShipLimitsCharacteristics entity)
        {
            await _shipLimitsCharacteristics.InsertAsync(entity);
        }

        public async Task InsertRangeAsync(IEnumerable<ShipLimitsCharacteristics> entity)
        {
            await _shipLimitsCharacteristics.InsertRangeAsync(entity);
            await _shipLimitsCharacteristics.SaveChanges();
        }

        public async Task<bool> IsExistAsync(Expression<Func<ShipLimitsCharacteristics, bool>> filter)
        {
            return await _shipLimitsCharacteristics.IsExistAsync(filter);
        }

        public async Task Update(ShipLimitsCharacteristics entityToUpdate)
        {
            _shipLimitsCharacteristics.Update(entityToUpdate);
            await _shipLimitsCharacteristics.SaveChanges();
        }
    }
}
