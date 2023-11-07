import mock
import unittest


class ShipTestCase(unittest.TestCase):
    @mock.patch('Ship.Ship')
    def test_sail(self, mock_ship):
        data = { "ship_id": "cfecaddc-a6df-4a74-ac43-a8032b124728",
        "port_id": "08f032a0-074c-4bbb-b859-98bc924ded22",
        "ports_deliver": "c2e68204-2e11-464f-abcf-6603585761db",
        "totalWeightCapacity": 1000,
        "maxNumberOfAllContainers": 20,
        "maxNumberOfHeavyContainers": 5,
        "maxNumberOfRefrigeratedContainers": 2,
        "maxNumberOfLiquidContainers": 5,
        "fuelConsumptionPerKM": 20}
        ship = mock_ship(data)
        ship.fuel = 0
        ship.max_fuel = 1000
        self.assertTrue(ship.refuel(100))
        print(ship.max_fuel)

        #self.assertFalse(ship.refuel(10000000))
    @mock.patch('Ship.Ship')
    def test_containers(self, mock_ship):
        data = { "ship_id": "cfecaddc-a6df-4a74-ac43-a8032b124728",
        "port_id": "08f032a0-074c-4bbb-b859-98bc924ded22",
        "ports_deliver": "c2e68204-2e11-464f-abcf-6603585761db",
        "totalWeightCapacity": 1000,
        "maxNumberOfAllContainers": 20,
        "maxNumberOfHeavyContainers": 5,
        "maxNumberOfRefrigeratedContainers": 2,
        "maxNumberOfLiquidContainers": 5,
        "fuelConsumptionPerKM": 20}
        ship = mock_ship(data)
        self.assertIsNotNone(ship.containers[0])

class PortTestCase(unittest.TestCase):
    @mock.patch('Port.Port')
    def test_container(self, mock_port):
        data ={ "port_id": "08f032a0-074c-4bbb-b859-98bc924ded22",
    "longitude": "41.33583199",
    "latitude": "2.151332728",
    "ships": [
      {
        "ship_id": "cfecaddc-a6df-4a74-ac43-a8032b124728",
        "port_id": "08f032a0-074c-4bbb-b859-98bc924ded22",
        "ports_deliver": "c2e68204-2e11-464f-abcf-6603585761db",
        "totalWeightCapacity": 1000,
        "maxNumberOfAllContainers": 20,
        "maxNumberOfHeavyContainers": 5,
        "maxNumberOfRefrigeratedContainers": 2,
        "maxNumberOfLiquidContainers": 5,
        "fuelConsumptionPerKM": 20
      },
      {
        "ship_id": "f740b708-e49a-4cd1-91b8-738db16b9d78",
        "port_id": "08f032a0-074c-4bbb-b859-98bc924ded22",
        "ports_deliver": "c2e68204-2e11-464f-abcf-6603585761db",
        "totalWeightCapacity": 1000,
        "maxNumberOfAllContainers": 20,
        "maxNumberOfHeavyContainers": 5,
        "maxNumberOfRefrigeratedContainers": 2,
        "maxNumberOfLiquidContainers": 5,
        "fuelConsumptionPerKM": 20
      }
    ],
    "basic": 8,
    "heavy": 3,
    "refrigerated": 5,
    "liquid": 3 }
        port = mock_port(data)
        container = port.create_container('B', 1000)
        port.create_container('B', 1000)
        self.assertIsNotNone(port.basic_containers[0])
