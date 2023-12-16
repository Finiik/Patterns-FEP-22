using lab4BL.Services.Implementation;
using lab4BL.Services.Interfaces;
using Lab4DataLayer.Entities;
using Microsoft.AspNetCore.Mvc;

namespace lab4.Controllers
{
    public class ItemController : Controller
    {
        private readonly IItemService _itemService;

        public ItemController(IItemService itemService)
        {
            _itemService = itemService;
        }

        [HttpGet]
        public ActionResult Get(int id)
        {
            return Ok(_itemService.GetAsync(id));
        }

        [HttpGet]
        public ActionResult GetAll()
        {
            return Ok(_itemService.GetAllAsync());
        }

        [HttpPost]
        public ActionResult Create([FromBody] Item item)
        {
            return Ok(_itemService.InsertAsync(item));
        }


        [HttpPost]
        public ActionResult Edit(Item item)
        {
            return Ok(_itemService.Update(item));
        }

        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Delete(Item item)
        {
            return Ok(_itemService.Delete(item));
        }
    }
}
