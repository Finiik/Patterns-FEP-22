import json
from uuid import uuid4
import random

# Generate unique port IDs
ports_id = [str(uuid4()) for _ in range(5)]

# Create a list of ships using a list comprehension and dictionary literals
ships = [{
    "ship_id": str(uuid4()),
    "port_id": random.choice(ports_id),
    "ports_deliver": random.choice([p for p in ports_id if p != ["port_id"]]),
    "total_weight_capacity": 1000,
    "max_number_of_all_containers": 20,
    "max_number_of_heavy_containers": 5,
    "max_number_of_refrigerated_containers": 2,
    "max_number_of_liquid_containers": 5,
    "fuel_consumption_per_km": 20
} for _ in range(10)]

# Create a list of ports
ports = []
for p_id in ports_id:
    port = {
        "port_id": p_id,
        "ships": [s for s in ships if s["port_id"] == p_id],
        "basic": random.randint(1, 10),
        "heavy": random.randint(1, 8),
        "refrigerated": random.randint(1, 5),
        "liquid": random.randint(1, 5)
    }
    ports.append(port)

# Convert the list of ports to a JSON object with indentation
json_object = json.dumps(ports, indent=2)

# Write the JSON object to a file named 'input.json'
with open('input.json', 'w') as outfile:
    outfile.write(json_object)
