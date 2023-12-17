from fastapi import APIRouter

# from app.api.routes.deliver import router as ship_router
from app.api.routes.ports import router as ports_router
from app.api.routes.initdb import router as initdb_router
from app.api.routes.index import router as index_router
from app.api.routes.deliver import router as deliver_router

router = APIRouter()
router.include_router(index_router, prefix="", tags=["index"])
router.include_router(ports_router, prefix="/ports", tags=["ports"])
router.include_router(initdb_router, prefix="/initdb", tags=["initdb"])
router.include_router(deliver_router, prefix="/deliver", tags=["deliver"])
# router.include_router(ship_router, prefix="/ships", tags=["ships"])
