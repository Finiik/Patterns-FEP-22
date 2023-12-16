using lab4BL.Services.Interfaces;
using Lab4DataLayer.Entities;
using Lab4DataLayer.Enums;
using Lab4DataLayer.Repositories;
using System.Linq.Expressions;

namespace lab4BL.Services.Implementation
{
    public class ContainerService : IContainerService
    {
        private readonly IRepository<Container> _containerRepository;
        public ContainerService(IRepository<Container> containerRepository)
        {
            _containerRepository = containerRepository;
        }

        public async Task AddItemToContainer(int id, Item item)
        {
            var container = await _containerRepository.GetAsync(id);
            container.Items.Add(item);
            await Update(container);
        }

        public async Task Delete(Container entityToDelete)
        {
            _containerRepository.Delete(entityToDelete);
            await _containerRepository.SaveChanges();
        }

        public async Task<IEnumerable<Container>> FilterAsync(Expression<Func<Container, bool>> filter)
        {
            return await _containerRepository.FilterAsync(filter);
        }

        public async Task<IEnumerable<Container>> GetAllAsync()
        {
            return await _containerRepository.GetAllAsync();
        }

        public async Task<Container> GetAsync(int id)
        {
            return await _containerRepository.GetAsync(id);
        }

        public async Task<double> GetConsumption(int id)
        {
            var item = await _containerRepository.GetAsync(id);
            return item.Fuel * item.Weight;
        }

        public async Task InsertAsync(Container entity)
        {
            if (entity.Weight < 300)
            {
                entity.ContainerType = ContainerTypes.BasicContainer;
            }
            entity.Fuel = GetContainerFuel(entity.ContainerType);

            await _containerRepository.InsertAsync(entity);
        }

        public async Task InsertRangeAsync(IEnumerable<Container> entity)
        {
           if (entity is null || !entity.Any())
           {
                return ;
           }

            foreach (var item in entity)
            {
                item.ContainerType = item.Weight > 300
                    ? item.ContainerType
                    : ContainerTypes.BasicContainer;

                item.Fuel = GetContainerFuel(item.ContainerType);
            }

            await _containerRepository.InsertRangeAsync(entity);
            await _containerRepository.SaveChanges();
        }

        public async Task<bool> IsExistAsync(Expression<Func<Container, bool>> filter)
        {
            return await _containerRepository.IsExistAsync(filter);
        }

        public async Task Update(Container entityToUpdate)
        {
            _containerRepository.Update(entityToUpdate);
            await _containerRepository.SaveChanges();
        }

        private double GetContainerFuel(ContainerTypes containerTypes)
        {
            switch (containerTypes)
            {
                case ContainerTypes.LiquidContainer: return 4.0;
                case ContainerTypes.RefrigeratedContainer: return 5.0;
                case ContainerTypes.HeavyContainer: return 3.5;
                default: return 2.5;
            }
        }
    }
}
