using lab4BL.Services.Implementation;
using lab4BL.Services.Interfaces;
using Lab4DataLayer.Entities;
using Microsoft.AspNetCore.Mvc;

namespace lab4.Controllers
{
    public class PortController : Controller
    {
        private readonly IPortService _portService;

        public PortController(IPortService portService)
        {
            _portService = portService;
        }

        [HttpGet]
        public ActionResult Get(int id)
        {
            return Ok(_portService.GetAsync(id));
        }

        [HttpGet]
        public ActionResult GetAll()
        {
            return Ok(_portService.GetAllAsync());
        }

        [HttpPost]
        public ActionResult Create([FromBody] Port item)
        {
            return Ok(_portService.InsertAsync(item));
        }

        [HttpPost]
        public ActionResult AddIncomingShip([FromBody] Ship ship, [FromQuery] int id)
        {
            return Ok(_portService.AddIncomingShip(ship,id));
        }

        [HttpPost]
        public ActionResult AddOutgoingShip([FromBody] Ship ship, [FromQuery] int id)
        {
            return Ok(_portService.AddOutgoingShip(ship, id));
        }

        [HttpPost]
        public ActionResult Edit(Port item)
        {
            return Ok(_portService.Update(item));
        }

        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Delete(Port item)
        {
            return Ok(_portService.Delete(item));
        }
    }
}
