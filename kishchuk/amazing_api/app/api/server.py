from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router as api_router
from app.db.database import Base, engine

Base.metadata.create_all(bind=engine)


def app_factory():
    app = FastAPI(title="The most amazing app you have ever seen", version="1.0.0")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(api_router, prefix="/api")
    print(f"The most amazing app you have ever seen")
    return app


app = app_factory()
