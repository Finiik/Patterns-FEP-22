from fastapi import APIRouter, Depends
from fastapi import HTTPException
from starlette import status
from app.schemas.port import Port
from app.db.database import get_db
from app.db.repositories.ports import PortRepository

from sqlalchemy.orm import Session

router = APIRouter()

""" 
@router.get("/update", status_code=status.HTTP_201_CREATED)
def update_port( db: Session = Depends(get_db)):
    port_crud = PortRepository(db_session=db)
    db_port = port_crud.get_by_id(port_id=1)
    if db_port:
        db_port = port_crud.update_port(port=db_port)
    else:
        raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Port does not exist"
    )
    return db_port
"""

@router.post("/", response_model=Port, status_code=status.HTTP_201_CREATED)
def create_ports(port: Port, db: Session = Depends(get_db)):
    port_crud = PortRepository(db_session=db)
    db_port = port_crud.get_by_id(port_id=port.id)
    if db_port:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Port already exist"
        )
    db_port = port_crud.create_port(port=port)
    return db_port


@router.get("/", response_model=list[Port], status_code=status.HTTP_200_OK)
def get_all_ports(db: Session = Depends(get_db)):
    print(f"===== get_all_ports =======")
    port_crud = PortRepository(db_session=db)
    print(f"port_crud.get_all_ports() {port_crud.get_all_ports()}")
    return port_crud.get_all_ports()
