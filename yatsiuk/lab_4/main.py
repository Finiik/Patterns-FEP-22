import json
from random import randint
from uuid import uuid4

from models import TablePort, TableShip, TableItem, TableContainer, session, engine
from container import Container
from fastapi import FastAPI, Depends, HTTPException
from port import Port, ContainersDetails
from ship import Ship, ConfigShip
from item import Item
from delivery import CreateItem, CreateContainer, CreateShip, CreatePort, DeliveryInput
from sqlalchemy import func

app = FastAPI()

with open('input_data.json', 'r') as file:
    data = json.load(file)

connection = engine.connect()


@app.post("/createPort", status_code=200)
def create_port(port: CreatePort):
    random_id = str(uuid4())
    new_port_dict = {
        "id": random_id,
        "latitude": port.latitude,
        "longitude": port.longitude,
        "basic_cont": port.basic_cont,
        "heavy_cont": port.heavy_cont,
        "refrigerated_cont": port.refrigerated_cont,
        "liquid_cont": port.liquid_cont
    }
    new_port = Port(id=random_id, latitude=port.latitude, longitude=port.longitude, data_cont=ContainersDetails(
        basic_cont=port.basic_cont, heavy_cont=port.heavy_cont, refrigerated_cont=port.refrigerated_cont,
        liquid_cont=port.liquid_cont))
    port = TablePort(random_id, new_port.latitude, new_port.longitude, new_port.basic_cont,
                     new_port.heavy_cont, new_port.refrigerated_cont, new_port.liquid_cont)
    session.add(port)
    session.commit()
    return new_port_dict


def determine_ship_type(ship: CreateShip) -> str:
    if ship.total_weight_capacity <= 20000:
        return "LightWeight"
    elif ship.total_weight_capacity <= 40000:
        return "Medium"
    elif ship.total_weight_capacity <= 60000:
        return "Heavy"
    else:
        return "Unknown"


@app.post("/createShip", status_code=200)
def create_ship(ship: CreateShip):
    random_id = str(uuid4())
    current_port_id = None
    port_ids_in_ship = [row[0] for row in session.query(TableShip.port_id).all()]
    port_ids_in_ports = [row[0] for row in session.query(TablePort.id).all()]
    port_rows_data = session.query(TablePort).all()
    if not port_ids_in_ship:
        current_port_id = port_ids_in_ports[0]
    else:
        current_port_id = port_ids_in_ports[randint(0, 2)]

    ship_type = determine_ship_type(ship)

    new_ship_dict = {
        "id": random_id,
        "fuel": ship.fuel,
        "ship_type": ship_type,
        "current_port": current_port_id,
        "total_weight_capacity": ship.total_weight_capacity,
        "max_all_containers": ship.maxNumberOfAllContainers,
        "max_basic_containers": ship.maxNumberOfBasicContainers,
        "max_heavy_containers": ship.maxNumberOfHeavyContainers,
        "max_refrigerated_containers": ship.maxNumberOfRefrigeratedContainers,
        "max_liquid_containers": ship.maxNumberOfLiquidContainers,
        "fuel_consumption_per_km": ship.fuelConsumptionPerKM
    }

    ship_to_db = TableShip(random_id, current_port_id, ship_type, ship.fuel, ship.total_weight_capacity,
                           ship.maxNumberOfAllContainers,
                           ship.maxNumberOfBasicContainers, ship.maxNumberOfHeavyContainers,
                           ship.maxNumberOfRefrigeratedContainers, ship.maxNumberOfLiquidContainers,
                           ship.fuelConsumptionPerKM)
    session.add(ship_to_db)
    session.commit()

    port_for_ship = None
    for row in port_rows_data:
        if row.id == current_port_id:
            port_for_ship = Port(id=row.id, latitude=row.latitude, longitude=row.longitude,
                                 data_cont=ContainersDetails(row.basic_cont, row.heavy_cont,
                                                             row.refrigerated_cont,
                                                             row.liquid_cont))

    new_ship = Ship(id=random_id, fuel=ship.fuel, current_port=port_for_ship, ship_type=ship_type,
                    ships_data=ConfigShip(
                        ship.total_weight_capacity, ship.maxNumberOfAllContainers, ship.maxNumberOfBasicContainers,
                        ship.maxNumberOfHeavyContainers, ship.maxNumberOfRefrigeratedContainers,
                        ship.maxNumberOfLiquidContainers,
                        ship.fuelConsumptionPerKM))
    return new_ship_dict


def get_latest_port_id():
    latest_port = session.query(Port).order_by(Port.id.desc()).first()
    if latest_port:
        return latest_port.id
    else:
        return None


@app.post("/createContainer", status_code=200)
def create_cont(container: Container, port_id: int = Depends(get_latest_port_id)):
    random_id = str(uuid4())

    container_type = Container.create_container(random_id, container.weight, container.type)

    cont_to_db = Container(
        id=random_id,
        port_id=port_id,
        weight=container.weight,
        type=container_type,
    )

    session.add(cont_to_db)
    session.commit()

    new_cont_dict = {
        "id": random_id,
        "weight": container.weight,
        "type": container_type,
        "port_id": port_id,
    }

    return new_cont_dict


def get_cont_id(item_type):
    specific_type_conts = session.query(TableContainer).filter(TableContainer.type == item_type).all()
    for cont in specific_type_conts:
        count = session.query(func.count()).filter(TableItem.container_id == cont.id).scalar()
        if count < 3:
            return cont.id


@app.post("/createItem", status_code=200)
def create_items(item: list[CreateItem]):
    item_list = []
    for item in item_list:
        try:
            random_id = str(uuid4())
            item_type = Item.check_type(random_id, item.weight, item.count)
            cont_id = get_cont_id(item.type)
            new_item_dict = {
                "id": random_id,
                "weight": item.weight,
                "type": item_type,
                "container_id": cont_id,
            }
            item_list.append(new_item_dict)
            cont_obj = TableItem(random_id, cont_id, item.weight, item.count, item.type)
            session.add(cont_obj)
        except HTTPException:
            continue
    session.commit()
    return item_list


@app.post('/Delivery', status_code=200)
def delivery(ids_data: DeliveryInput):

    starting_port = session.query(TablePort).filter(TablePort.id == ids_data.starting_port_id).first()
    transitional_port = session.query(TablePort).filter(TablePort.id == ids_data.transitional_port_id).first()
    ending_port = session.query(TablePort).filter(TablePort.id == ids_data.ending_port_id).first()
    all_ports = [starting_port, ending_port, transitional_port]

    ship_to_sail = session.query(TableShip).filter(TableShip.id == ids_data.ship_to_sail_id).first()

    conts_in_start_port = [row for row in
                           session.query(TableContainer).filter(TableContainer.port_id == starting_port.id).all()]
    conts_in_end_port = [row for row in
                         session.query(TableContainer).filter(TableContainer.port_id == ending_port.id).all()]

    conts_in_port_id = [row for row in
                        session.query(TableContainer.id).filter(TableContainer.port_id == starting_port.id).all()]
    all_items = session.query(TableItem).all()
    item_packs = [row for row in all_items if row.container_id in conts_in_port_id]

    for i, port in enumerate(all_ports):
        port_obj = Port(id=port.id, latitude=port.latitude, longitude=port.longitude)
        all_ports[i] = port_obj

    if ship_to_sail.port_id == starting_port.id:
        ship_obj = Ship.check_type(id=ship_to_sail.id, fuel=ship_to_sail.fuel, current_port=all_ports[0],
                                   ships_data=ConfigShip(
                                       ship_to_sail.total_weight_capacity, ship_to_sail.max_all_cont,
                                       ship_to_sail.max_basic_cont,
                                       ship_to_sail.max_heavy_cont, ship_to_sail.max_refrigerated_cont,
                                       ship_to_sail.max_liquid_cont,
                                       ship_to_sail.fuel_consumption_per_km))
        all_ports[0].ship_current.append(ship_obj)
    else:
        raise HTTPException(status_code=404, detail="Given ship isn't in given port")


    all_conts = []
    all_conts_for_result = []
    for cont in conts_in_start_port:
        cont_obj = Container.check_category(id=cont.id, weight=cont.weight, type=cont.type)
        all_conts.append(cont_obj)
        all_ports[0].containers.append(cont_obj)
    for cont in conts_in_end_port:
        cont_obj = Container.check_category(id=cont.id, weight=cont.weight, type=cont.type)
        all_ports[1].containers.append(cont_obj)
        all_conts_for_result.append(all_ports[1].containers)

    all_packs_of_items = []
    for pack in item_packs:
        pack_obj = Item.check_type(id=pack.id, weight=pack.weight, count=pack.count, item_type=pack.type,
                                    container_id=pack.container_id)
        all_packs_of_items.append(pack_obj)

    for pack in all_packs_of_items:
        for cont in all_conts:
            if cont.id == pack.container_id:
                cont.items.append(pack)
                cont.weight += pack.getTotalWeight()

    temp_copy = list(ship_obj.current_port.containers)
    for cont in temp_copy:
        ship_obj.load(cont)

    ship_obj.sail_to(all_ports[0], all_ports[1], all_ports[2])
    row_to_update = session.query(TableShip).filter(TableShip.port_id == starting_port.id).first()
    row_to_update.port_id = ending_port.id
    session.commit()

    for _ in ship_obj.containers:
        row_to_update = session.query(TableContainer).filter(TableContainer.port_id == starting_port.id).first()
        row_to_update.port_id = ending_port.id
        session.commit()
        session.close()

    while ship_obj.containers:
        ship_obj.unload(ship_obj.containers[0])
    return (f"Amount of containers before delivery: {len(all_conts_for_result)}. "
            f"Amount of containers after delivery: {len(all_ports[1].containers)}. Delivery was successful! ")
