using lab4BL.Services.Interfaces;
using Lab4DataLayer.Entities;
using Microsoft.AspNetCore.Mvc;

namespace lab4.Controllers
{
    public class ContainerController : Controller
    {
        private readonly IContainerService _containerService;

        public ContainerController(IContainerService containerService)
        {
            _containerService = containerService;
        }

        [HttpGet]
        public ActionResult Get(int id)
        {
            return Ok(_containerService.GetAsync(id));
        }

        [HttpGet]
        public ActionResult GetAll()
        {
            return Ok(_containerService.GetAllAsync());
        }

        [HttpPost]
        public ActionResult Create([FromBody] Container item)
        {
            return Ok(_containerService.InsertAsync(item));
        }

        [HttpPost]
        public ActionResult AddItemToContainer([FromQuery]int id, [FromBody]Item item)
        {
            return Ok(_containerService.AddItemToContainer(id, item));
        }


        [HttpPost]
        public ActionResult Edit(Container item)
        {
            return Ok(_containerService.Update(item));
        }

        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Delete(Container item)
        {
            return Ok(_containerService.Delete(item));
        }
    }
}
