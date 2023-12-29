using Microsoft.AspNetCore.Mvc;

namespace Empty.Controllers
{
    public class HomeController : Controller
    {
        [HttpGet]
        public IActionResult Index()
        {
            return Redirect("~/swagger/index.html");
        }
    }
}