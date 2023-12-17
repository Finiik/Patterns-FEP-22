from fastapi import APIRouter, Depends
from fastapi import HTTPException
from starlette import status
from app.schemas.port import Port
from app.schemas.ship import *
from app.schemas.containers import *
from app.db.database import get_db
from app.db.repositories.ports import PortRepository
from app.db.repositories.ships import ShipRepository
from app.db.repositories.containers import ContainerRepository
import json
import random

from sqlalchemy.orm import Session

router = APIRouter()


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
def initdb(db: Session = Depends(get_db)):
    print(f"===== initdb =======")
    port_crud = PortRepository(db_session=db)
    ship_crud = ShipRepository(db_session=db)
    container_crud = ContainerRepository(db_session=db)
    # Зчитуємо JSON з файлу
    with open("input_2.json") as input_file:
        data = json.load(input_file)

    ####        append ports         ####
    print(f"\nappend ports and ships\n")

    i = 0
    cont_id = 1
    for port_data in data["ports"]:
        port_id = port_data["port_id"]
        title = port_data["title"]
        basic = port_data["basic"]
        heavy = port_data["heavy"]
        refrigerated = port_data["refrigerated"]
        liquid = port_data["liquid"]
        latitude = random.uniform(30.0, 32.0)
        longitude = random.uniform(20.0, 22.0)

        port = Port(id=port_id,title=title, basic=basic, heavy=heavy,
                    refrigerated=refrigerated, liquid=liquid, latitude=latitude,
                    longitude=longitude)

        db_port = port_crud.get_by_id(port_id=port.id)
        if db_port:
            print(f"Port already exist")
        else:
            db_port = port_crud.create_port(port=port)
            print(f"Port created {port}")

         ####        append ships         ####
        ships = port_data["ships"]
        for j in range(0, len(ships)):
            ship_data = ships[j]
            ship_id = ship_data["ship_id"]
            port_deliver_id = ship_data["ports_deliver"]
            fuel = ship_data["fuel"]
            port = ship_data["port_id"]
            totalWeightCapacity = ship_data["totalWeightCapacity"]
            maxNumberOfAllContainers = ship_data["maxNumberOfAllContainers"]
            maxNumberOfHeavyContainers = ship_data["maxNumberOfHeavyContainers"]
            maxNumberOfRefrigeratedContainers = ship_data["maxNumberOfRefrigeratedContainers"]
            maxNumberOfLiquidContainers = ship_data["maxNumberOfLiquidContainers"]
            maxNumberOfBasicContainers = ship_data["maxNumberOfBasicContainers"]
            fuelConsumptionPerKM = ship_data["fuelConsumptionPerKM"]
            ship_type = ship_data["ship_type"]
            ship_title = ship_data["title"]

            print(f"Ship creating")
            print(f"Ship id: {ship_id}")
            print(f"Title: {ship_title}")
            ship = IShip(type_=ship_type, id=ship_id, port_id=port, title=ship_title, fuel=fuel,
                         port_deliver=port_deliver_id,
                         total_weight_capacity=totalWeightCapacity,
                         max_number_of_all_containers=maxNumberOfAllContainers,
                         max_number_of_basic_containers=maxNumberOfBasicContainers,
                         max_number_of_heavy_containers=maxNumberOfHeavyContainers,
                         max_number_of_refrigerated_containers=maxNumberOfRefrigeratedContainers,
                         max_number_of_liquid_containers=maxNumberOfLiquidContainers,
                         fuel_consumption_per_km=fuelConsumptionPerKM)

            print(f"ship_crud.get_by_id : {ship.id}")
            db_ship = ship_crud.get_by_id(ship.id)
            if db_ship:
                print(f"Ship already exist")
            else:
                 db_ship = ship_crud.create_ship(ship=ship)
                 print(f"Ship {ship} created")

        ####        append containers         ####


        for count in range(0, basic):
            container = BasicContainer(id=cont_id, weight=random.uniform(10.0, 15.0), port_id=port_id, ship_id=-1)
            db_container = container_crud.get_by_id(container.id)
            if db_container:
                print(f"Container already exist")
            else:
                db_container = container_crud.create_container(container=container)
                print(f"Container {container} created")
                cont_id += 1

                # print(f"Item {real_basic.items} created")

        for count in range(0, heavy):
            container = HeavyContainer(id=cont_id, weight=random.uniform(10.0, 20.0), port_id=port_id, ship_id=-1)
            db_container = container_crud.get_by_id(container.id)
            if db_container:
                print(f"Container already exist")
            else:
                db_container = container_crud.create_container(container=container)
                print(f"Container {container} created")
                cont_id += 1
                # print(f"Item {real_heavy.items} created")

        for count in range(0, refrigerated):
            container = RefrigeratedContainer(id=cont_id, weight=random.uniform(10.0, 20.0), port_id=port_id, ship_id=-1)
            db_container = container_crud.get_by_id(container.id)
            if db_container:
                print(f"Container already exist")
            else:
                db_container = container_crud.create_container(container=container)
                print(f"Container {container} created")
                cont_id += 1


                # print(f"Item {real_refrigerated.items} created")

        for count in range(0, liquid):
            container = LiquidContainer(id=cont_id, weight=random.uniform(10.0, 20.0), port_id=port_id, ship_id=-1)
            db_container = container_crud.get_by_id(container.id)
            if db_container:
                print(f"Container already exist")
            else:
                db_container = container_crud.create_container(container=container)
                print(f"Container {container} created")
                cont_id += 1

                # print(f"Item {real_liquid.items} created")

    i = i + 1

        #ports_list.append(Port(port_id, latitude, longitude))
        #ships = port_data["ships"]
    print(f"port list = {port_crud.get_all_ports()}")
    return port_crud.get_all_ports()
