from typing import List
from fastapi import APIRouter, Depends
from fastapi import HTTPException
from starlette import status
from app.schemas.port import Port
from app.schemas.containers import *
from app.schemas.ship import IShip
from app.db.database import get_db
from app.db.repositories.ports import PortRepository
from app.db.repositories.ships import ShipRepository
from app.db.repositories.containers import ContainerRepository


from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/", response_model=IShip, status_code=status.HTTP_201_CREATED)
def create_ports(ship: IShip, db: Session = Depends(get_db)):
    ship_crud = ShipRepository(db_session=db)
    db_ship = ship_crud.get_by_id(ship_id=ship.id)
    if db_ship:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ship already exist"
        )
    db_ship = ship_crud.create_ship(ship=ship)
    return db_ship

@router.get("/ship_list", status_code=status.HTTP_200_OK)
def get_all_ships(db: Session = Depends(get_db)):
    print(f"===== get_all_ships =======")
    ship_crud = ShipRepository(db_session=db)
    print(f"get ships info")
    result = ship_crud.get_all_ships()
    return result

@router.get("/load_cont", status_code=status.HTTP_200_OK)
def load_containers(db: Session = Depends(get_db)):
    print(f"===== load_containers =======")
    ship_crud = ShipRepository(db_session=db)
    container_crud = ContainerRepository(db_session=db)


    # 4. Ships can load() containers
    print(f"\nShips load containers\n")
    ship_list:list[IShip] = ship_crud.get_all_ships()
    for i in range(0, len(ship_list)):
        cur_ship = ship_list[i]

        a_ship = IShip(id=cur_ship.id,
                       title=cur_ship.title, type_=cur_ship.type_, fuel=cur_ship.fuel, port_id=cur_ship.port_id,
                       port_deliver=cur_ship.port_deliver_id,
                       total_weight_capacity=cur_ship.total_weight_capacity,
                       max_number_of_all_containers=cur_ship.max_number_of_all_containers,
                       max_number_of_basic_containers=cur_ship.max_number_of_basic_containers,
                       max_number_of_heavy_containers=cur_ship.max_number_of_heavy_containers,
                       max_number_of_refrigerated_containers=cur_ship.max_number_of_refrigerated_containers,
                       max_number_of_liquid_containers=cur_ship.max_number_of_liquid_containers,
                       fuel_consumption_per_km=cur_ship.fuel_consumption_per_km
                       )
        print(f"ship: {a_ship}\n")

        container_list = container_crud.get_containers_by_port(a_ship.port_id)
        print(f"container in port : {len(container_list)}\n")
        cont_count = 0
        heavy_cont = 0
        basic_cont = 0
        liquid_cont = 0
        refrigerated_cont = 0
        for j in range(0, len(container_list)):
            a_cont = container_list[j]
            #print(f"container: {a_cont}")

            if (a_cont.type == "heavy") & (a_ship.max_number_of_heavy_containers >= heavy_cont):
                a_ship.load(db, a_cont)
                heavy_cont +=1
            elif (a_cont.type == "basic") & (a_ship.max_number_of_basic_containers >= basic_cont):
                a_ship.load(db, a_cont)
                basic_cont +=1
            elif (a_cont.type == "liquid") & (a_ship.max_number_of_liquid_containers >= liquid_cont):
                a_ship.load(db, a_cont)
                liquid_cont +=1
            elif (a_cont.type == "refrigerated") & (a_ship.max_number_of_refrigerated_containers >= refrigerated_cont):
                a_ship.load(db, a_cont)
                refrigerated_cont +=1
            else:
                print(f"unknown container type\n")

        count = heavy_cont+basic_cont+refrigerated_cont+liquid_cont
        print(f"load {count}  cont, in ship {a_ship}\n")

    return ship_list

@router.get("/sail_ships", status_code=status.HTTP_200_OK)
def sail_ships(db: Session = Depends(get_db)):
    print(f"===== sail_ships =======")

    ship_crud = ShipRepository(db_session=db)

    # 5. Ships sail to ports()
    print(f"\nShips sail to ports\n")
    ship_list: list[IShip] = ship_crud.get_all_ships()
    for i in range(0, len(ship_list)):
        cur_ship = ship_list[i]

        a_ship = IShip(id=cur_ship.id,
                       title=cur_ship.title, type_=cur_ship.type_, fuel=cur_ship.fuel, port_id=cur_ship.port_id,
                       port_deliver=cur_ship.port_deliver_id,
                       total_weight_capacity=cur_ship.total_weight_capacity,
                       max_number_of_all_containers=cur_ship.max_number_of_all_containers,
                       max_number_of_basic_containers=cur_ship.max_number_of_basic_containers,
                       max_number_of_heavy_containers=cur_ship.max_number_of_heavy_containers,
                       max_number_of_refrigerated_containers=cur_ship.max_number_of_refrigerated_containers,
                       max_number_of_liquid_containers=cur_ship.max_number_of_liquid_containers,
                       fuel_consumption_per_km=cur_ship.fuel_consumption_per_km
                       )
        print(f"ship: {a_ship}\n")

        if not a_ship.sail_to(db):
            a_ship.fuel += 10000000
            a_ship.sail_to(db)
            #print(f"ship {a_ship} sailed to port {a_ship.port_id}")

    return ship_list

@router.get("/unload_cont", status_code=status.HTTP_200_OK)
def unload_containers(db: Session = Depends(get_db)):
    print(f"===== unload_containers =======")
    ship_crud = ShipRepository(db_session=db)
    container_crud = ContainerRepository(db_session=db)


    # 4. Ships can unload() containers
    print(f"\nShips unload containers\n")
    ship_list:list[IShip] = ship_crud.get_all_ships()
    for i in range(0, len(ship_list)):
        cur_ship = ship_list[i]

        a_ship = IShip(id=cur_ship.id,
                       title=cur_ship.title, type_=cur_ship.type_, fuel=cur_ship.fuel, port_id=cur_ship.port_id,
                       port_deliver=cur_ship.port_deliver_id,
                       total_weight_capacity=cur_ship.total_weight_capacity,
                       max_number_of_all_containers=cur_ship.max_number_of_all_containers,
                       max_number_of_basic_containers=cur_ship.max_number_of_basic_containers,
                       max_number_of_heavy_containers=cur_ship.max_number_of_heavy_containers,
                       max_number_of_refrigerated_containers=cur_ship.max_number_of_refrigerated_containers,
                       max_number_of_liquid_containers=cur_ship.max_number_of_liquid_containers,
                       fuel_consumption_per_km=cur_ship.fuel_consumption_per_km
                       )
        print(f"ship: {a_ship}\n")

        container_list = container_crud.get_containers_by_ship(a_ship.id)
        print(f"container in port : {len(container_list)}\n")

        # 4. Ships unload containers
        print(f"\nShips unload containers\n")

        for j in range(0, len(container_list)):
            a_cont = container_list[j]

            a_ship.unload(db, a_cont)
            print(f"now {a_cont} unload")
    return ship_list