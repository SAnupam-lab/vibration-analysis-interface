"""

Dashboard API

"""

# Importing packages and modules
from fastapi import APIRouter, Request
from sources.classes.dao import DAO
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# Setting the template
templates = Jinja2Templates(directory="sources/templates/pages")

# Setting the route
router = APIRouter(prefix="/dashboard", tags=["dashboard"])

# Endpoint
@router.get("/", response_class=HTMLResponse)
async def open_dashboard(request: Request):
    dao = DAO()
    datasets = dao.read_datasets()
    return templates.TemplateResponse("dashboard.html", {"request": request, "datasets": datasets})