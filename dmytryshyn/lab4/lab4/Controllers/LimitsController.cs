using lab4BL.Services.Interfaces;
using Lab4DataLayer.Entities;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;

namespace lab4.Controllers
{
    public class LimitsController : Controller
    {
        private readonly ILimitsService _limitsService;

        public LimitsController(ILimitsService limitsService)
        {
            _limitsService = limitsService;
        }

        [HttpGet]
        public ActionResult Get(int id)
        {
            return Ok(_limitsService.GetAsync(id));
        }

        [HttpGet]
        public ActionResult GetAll()
        {
            return Ok(_limitsService.GetAllAsync());
        }

        [HttpPost]
        public ActionResult Create([FromBody] ShipLimitsCharacteristics item)
        {
            return Ok(_limitsService.InsertAsync(item));
        }


        [HttpPost]
        public ActionResult Edit(ShipLimitsCharacteristics item)
        {
            return Ok(_limitsService.Update(item));
        }

        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Delete(ShipLimitsCharacteristics item)
        {
            return Ok(_limitsService.Delete(item));
        }
    }
}
