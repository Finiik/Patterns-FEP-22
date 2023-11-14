using Lab4DataLayer.Entities;
using Microsoft.EntityFrameworkCore;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lab4DataLayer.Data
{
    public class lab4DbContext : DbContext
    {
        public lab4DbContext(DbContextOptions<lab4DbContext> options) : base(options)
        {
        }

        public DbSet<Item> Items { get; set; }
        public DbSet<Container> Containers { get; set; }
        public DbSet<Ship> Ships { get; set; }
        public DbSet<Port> Ports { get; set; }
        public DbSet<ShipLimitsCharacteristics> ShipLimitsCharacteristics { get; set; }


    }
}
