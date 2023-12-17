from fastapi import APIRouter, Depends
from fastapi import HTTPException
from starlette import status
from app.schemas.port import Port
from app.db.database import get_db
from app.db.repositories.ports import PortRepository
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from sqlalchemy.orm import Session

router = APIRouter()


templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})