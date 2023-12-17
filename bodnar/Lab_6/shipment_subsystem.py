class Shipment:
    def __init__(self):
        self.shipment_providers = []

    def create_shipment(self, destination: str):
        if not self.shipment_providers:
            print("Error: No shipment providers available.")
            return

        print(f"Shipment created successfully!")
        print(f"Destination: {destination}")

        selected_provider = self.shipment_providers[0]

        print(f"Selected Shipment Provider: {selected_provider.name}")

    def add_provider(self, provider: "ShipmentProvider"):
        self.shipment_providers.append(provider)
        print(f"Shipment provider '{provider.name}' added successfully.")


class ShipmentProvider:
    def __init__(self, name: str):
        self.name = name

    def add_provider(self, shipment: "Shipment"):
        shipment.shipment_providers.append(self)
        print(f"Shipment provider '{self.name}' added successfully.")

    def modify_provider(self, new_name: str):
        self.name = new_name
        print(f"Shipment provider updated. New name: {new_name}")
