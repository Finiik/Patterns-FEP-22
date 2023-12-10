from fastapi import APIRouter

# from app.api.routes.deliver import router as ship_router
from app.api.routes.ports import router as ports_router

router = APIRouter()
router.include_router(ports_router, prefix="/ports", tags=["ports"])
# router.include_router(ship_router, prefix="/ships", tags=["ships"])
