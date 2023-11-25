from fastapi import APIRouter

# from app.api.routes.deliver import router as ship_router


from app.api.routes.index import router as index_router
from app.api.routes.bankcustomer import router as bankcustomer_router

router = APIRouter()
router.include_router(index_router, prefix="", tags=["index"])
router.include_router(bankcustomer_router, prefix="/bankcustomer", tags=["bankcustomer"])

# router.include_router(ship_router, prefix="/ships", tags=["ships"])
