using lab4BL.Services.Implementation;
using lab4BL.Services.Interfaces;
using Lab4DataLayer.Entities;
using Lab4DataLayer.Repositories;

namespace lab4
{
    public class Program
    {
        public static void Main(string[] args)
        {
            var builder = WebApplication.CreateBuilder(args);

            // Add services to the container.
            builder.Services.AddControllersWithViews();
            builder.Services.AddTransient<IRepository<Ship>, Repository<Ship>>();
            builder.Services.AddTransient<IRepository<ShipLimitsCharacteristics>, Repository<ShipLimitsCharacteristics>>();
            builder.Services.AddTransient<IRepository<Item>, Repository<Item>>();
            builder.Services.AddTransient<IRepository<Port>, Repository<Port>>();
            builder.Services.AddTransient<IRepository<Container>, Repository<Container>>();
            builder.Services.AddTransient<IContainerService, ContainerService>();
            builder.Services.AddTransient<IItemService, ItemsService>();
            builder.Services.AddTransient<IPortService, PortService>();
            builder.Services.AddTransient<IShipService, ShipService>();
            builder.Services.AddTransient<ILimitsService, LimitsService>();

            var app = builder.Build();

            // Configure the HTTP request pipeline.
            if (!app.Environment.IsDevelopment())
            {
                app.UseExceptionHandler("/Home/Error");
                // The default HSTS value is 30 days. You may want to change this for production scenarios, see https://aka.ms/aspnetcore-hsts.
                app.UseHsts();
            }

            app.UseHttpsRedirection();
            app.UseStaticFiles();

            app.UseRouting();

            app.UseAuthorization();

            app.MapControllerRoute(
                name: "default",
                pattern: "{controller=Home}/{action=Index}/{id?}");

            app.Run();
        }
    }
}