import json
from uuid import uuid4

from port import Port, ContainerDetails

with open('input_data.json') as file:
    project_data = json.load(file)

Ports = []
for port_data in project_data["Ports_data"]:
    port = Port(
        id=str(uuid4()),
        latitude=port_data["latitude"],
        longitude=port_data["longitude"],
        data_cont=ContainerDetails(
            basic_cont=port_data["basic_cont"],
            heavy_cont=port_data["heavy_cont"],
            refrigerated_cont=port_data["refrigerated_cont"],
            liquid_cont=port_data["liquid_cont"]
        )
    )
    Ports.append(port)

# ... (rest of the code remains the same)
