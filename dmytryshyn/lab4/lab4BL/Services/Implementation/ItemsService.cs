using lab4BL.Services.Interfaces;
using Lab4DataLayer.Entities;
using Lab4DataLayer.Enums;
using Lab4DataLayer.Repositories;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Linq.Expressions;
using System.Text;
using System.Threading.Tasks;

namespace lab4BL.Services.Implementation
{
    public class ItemsService : IItemService
    {
        private readonly IRepository<Item> _itemRepository;

        public ItemsService(IRepository<Item> itemRepository)
        {
            _itemRepository = itemRepository;
        }
        public async Task Delete(Item entityToDelete)
        {
            _itemRepository.Delete(entityToDelete);
            await _itemRepository.SaveChanges();
        }

        public async Task<IEnumerable<Item>> FilterAsync(Expression<Func<Item, bool>> filter)
        {
            return await _itemRepository.FilterAsync(filter);
        }

        public async Task<IEnumerable<Item>> GetAllAsync()
        {
            return await _itemRepository.GetAllAsync();
        }

        public async Task<Item> GetAsync(int id)
        {
            return await _itemRepository.GetAsync(id);
        }

        public async Task InsertAsync(Item entity)
        {
            await _itemRepository.InsertAsync(entity);
        }

        public async Task InsertRangeAsync(IEnumerable<Item> entity)
        {
            await _itemRepository.InsertRangeAsync(entity);
            await _itemRepository.SaveChanges();
        }

        public async Task<bool> IsExistAsync(Expression<Func<Item, bool>> filter)
        {
            return await _itemRepository.IsExistAsync(filter);
        }

        public async Task Update(Item entityToUpdate)
        {
            _itemRepository.Update(entityToUpdate);
            await _itemRepository.SaveChanges();
        }
    }
}
