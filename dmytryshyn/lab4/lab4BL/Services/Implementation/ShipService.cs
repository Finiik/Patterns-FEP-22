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
    public class ShipService : IShipService
    {
        private readonly IRepository<Ship> _shipRepository;

        public ShipService(IRepository<Ship> shipRepository)
        {
            _shipRepository = shipRepository;
        }

        public async Task AddContainers(Container container, int id)
        {
            var ship = await _shipRepository.GetAsync(id);
            if (!CheckCapacity(container, ship.Containers.ToList(), ship.Characteristics))
            {
                return;
            }
            else
            {
                ship.Containers.Add(container);
                await Update(ship);
            }
        }

        public async Task Delete(Ship entityToDelete)
        {
            _shipRepository.Delete(entityToDelete);
            await _shipRepository.SaveChanges();
        }

        public async Task<IEnumerable<Ship>> FilterAsync(Expression<Func<Ship, bool>> filter)
        {
            return await _shipRepository.FilterAsync(filter);
        }

        public async Task<IEnumerable<Ship>> GetAllAsync()
        {
            return await _shipRepository.GetAllAsync();
        }

        public async Task<Ship> GetAsync(int id)
        {
            return await _shipRepository.GetAsync(id);
        }

        public async Task InsertAsync(Ship entity)
        {
            await _shipRepository.InsertAsync(entity);
        }

        public async Task InsertRangeAsync(IEnumerable<Ship> entity)
        {
            await _shipRepository.InsertRangeAsync(entity);
            await _shipRepository.SaveChanges();
        }

        public async Task<bool> IsExistAsync(Expression<Func<Ship, bool>> filter)
        {
            return await _shipRepository.IsExistAsync(filter);
        }

        public async Task<bool> Load(int shipId, int containerId)
        {
            var ship = await _shipRepository.GetAsync(shipId);

            return ship
                .Containers
                .Any(i => i.Id == containerId);
        }

        public async Task ReFuel(double newFuel, int id)
        {
            var ship = await _shipRepository.GetAsync(id);
            ship.Fuel = newFuel;
            await Update(ship);
        }

        public async Task RemoveContainers(int shipId, int containerId)
        {
            var ship = await _shipRepository.GetAsync(shipId);
            var container = ship.Containers.FirstOrDefault(i => i.Id == containerId);
            if (container != null)
            {
                ship.Containers.Remove(container);
                await Update(ship);
            }
        }

        public async Task<bool> SailTo(Port port, int id)
        {
            var ship = await _shipRepository.GetAsync(id);
            return ship.Port == port;
        }

        public async Task<bool> UnLoad(int shipId, int containerId)
        {
            var result  = await Load(shipId, containerId);
            return !result;
        }

        public async Task Update(Ship entityToUpdate)
        {
            _shipRepository.Update(entityToUpdate);
            await _shipRepository.SaveChanges();
        }

        private bool CheckCapacity(Container container, List<Container> Containers, ShipLimitsCharacteristics ShipLimitsCharacteristics)
        {
            var isUnderMaxCapacity = Containers.Count <= ShipLimitsCharacteristics.MaxNumberOfAllContainers;
            var isUnderMaxWeight = Containers.Sum(x => x.Weight) + container.Weight >= ShipLimitsCharacteristics.TotalWeightCapacity;

            var isUnderHeavyContainerCapacity =
                container.ContainerType is ContainerTypes.HeavyContainer
                    && Containers
                    .Where(x => x.ContainerType is ContainerTypes.HeavyContainer)
                    .Count() < ShipLimitsCharacteristics.MaxNumberOfHeavyContainers;

            var isUnderLiquidContainerCapacity =
                container.ContainerType is ContainerTypes.LiquidContainer
                    && Containers
                    .Where(x => x.ContainerType is ContainerTypes.LiquidContainer)
                    .Count() < ShipLimitsCharacteristics.MaxNumberOfLiquidContainers;

            var isUnderRefrigeratedContainerCapacity =
                container.ContainerType is ContainerTypes.RefrigeratedContainer
                         && Containers
                        .Where(x => x.ContainerType is ContainerTypes.RefrigeratedContainer)
                        .Count() < ShipLimitsCharacteristics.MaxNumberOfRefrigeratedContainers;

            return isUnderMaxCapacity
                && isUnderMaxWeight
                && (isUnderHeavyContainerCapacity
                || isUnderLiquidContainerCapacity
                || isUnderRefrigeratedContainerCapacity);
        }
    }
}
