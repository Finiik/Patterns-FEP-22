# shipment_subs.py (Bookstore Shipment)
class BookShipmentProvider:
    def __init__(self, name: str):
        self.name = name

    def modify_provider(self, new_name: str):
        self.name = new_name
        print(f"Shipment provider updated. New name: {new_name}")


class BookShipment:
    def __init__(self):
        self.shipment_providers = []

    def add_provider(self, provider: BookShipmentProvider):
        self.shipment_providers.append(provider)
        print(f"Shipment provider '{provider.name}' added successfully.")

    def create_shipment(self, delivery_address: str, weight: float):
        if not self.shipment_providers:
            print("Error: No shipment providers available.")
            return

        print(f"Shipment created successfully!")
        print(f"Delivery Address: {delivery_address}")
        print(f"Weight: {weight} kg")

        selected_provider = self.select_shipment_provider()

        if selected_provider:
            print(f"Selected Shipment Provider: {selected_provider.name}")
        else:
            print("Error: No shipment provider selected.")

    def select_shipment_provider(self):
        # Implement logic to select the best provider based on your criteria.
        # For now, it just selects the first provider in the list.
        return self.shipment_providers[0] if self.shipment_providers else None


class Shipment:
    def create_shipment(self, delivery_address, weight):
        pass
