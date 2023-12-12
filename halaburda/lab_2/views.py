# views.py
from app.controllers import ShipController
from app.schemas import ShipCreate
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()
ship_controller = ShipController()


@app.post("/create_ship")
def create_ship(ship_data: ShipCreate):
    result = ship_controller.create_ship(ship_data)
    return JSONResponse(content=result)


@app.post("/deliver")
def deliver_cargo(shipment_data: dict):
    result = ship_controller.deliver_cargo(shipment_data)
    return JSONResponse(content=result)


@app.get("/get_state_ship/{ship_id}")
def get_ship_state(ship_id: int):
    result = ship_controller.get_ship_state(ship_id)
    return JSONResponse(content=result)
