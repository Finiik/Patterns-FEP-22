using lab4BL.Services.Interfaces;
using Lab4DataLayer.Entities;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;

namespace lab4.Controllers
{
    public class ShipController : Controller
    {
        private readonly IShipService _shipService;

        public ShipController(IShipService shipService)
        {
            _shipService = shipService;
        }

        [HttpGet]
        public ActionResult Get(int id)
        {
            return Ok(_shipService.GetAsync(id));
        }

        [HttpGet]
        public ActionResult GetAll()
        {
            return Ok(_shipService.GetAllAsync());
        }

        [HttpPost]
        public ActionResult Create([FromBody] Ship ship)
        {
            return Ok(_shipService.InsertAsync(ship));
        }


        [HttpPost]
        public ActionResult Edit(Ship ship)
        {
           return Ok(_shipService.Update(ship));
        }

        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Delete(Ship ship)
        {
            return Ok(_shipService.Delete(ship));
        }

        [HttpPost]
        public ActionResult AddContainers(Container ship, int id)
        {
            return Ok(_shipService.AddContainers(ship,id));
        }

        [HttpPost]
        public ActionResult RemoveContainers(int shipId, int containerId)
        {
            return Ok(_shipService.RemoveContainers(shipId, containerId));
        }
    }
}
