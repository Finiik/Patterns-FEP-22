
using System.Linq.Expressions;


namespace Lab4DataLayer.Repositories
{
    public interface IRepository<T> where T : class
    {
        Task<IEnumerable<T>> FilterAsync(Expression<Func<T, bool>> filter);

        Task<IEnumerable<T>> GetAllAsync();

        Task<T> GetAsync(int id);

        Task InsertAsync(T entity);

        void Delete(T entityToDelete);

        void Update(T entityToUpdate);

        Task<bool> IsExistAsync(Expression<Func<T, bool>> filter);

        Task InsertRangeAsync(IEnumerable<T> entity);

        Task SaveChanges();
    }
}
