from fastapi import APIRouter, Depends
from fastapi import HTTPException
from starlette import status
from app.schemas.container import Container
from app.db.database import get_db
from app.db.repositories.containers import ContainerRepository

from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/", response_model=Container, status_code=status.HTTP_201_CREATED)
def create_container(container: Container, db: Session = Depends(get_db)):
    container_crud = ContainerRepository(db_session=db)
    db_container = container_crud.get_by_id(container_id=container.id)
    if db_container:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Container already exist"
        )
    db_container = container_crud.create_container(container=container)
    return db_container


@router.get("/", response_model=list[Container], status_code=status.HTTP_200_OK)
def get_all_containers(db: Session = Depends(get_db)):
    container_crud = ContainerRepository(db_session=db)
    return container_crud.get_all_containers()
