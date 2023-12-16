class Payment:
    def __init__(self):
        self.card_details = {}

    def add_card_details(self, card_number: str, expiration_date: str, cvv: int):
        self.card_details = {
            'card_number': card_number,
            'expiration_date': expiration_date,
            'cvv': hash(cvv)
        }
        print("Card details added successfully.")

    def verify_payment(self, total_amount: float):
        if self.card_details:
            print(f"Payment verified for total amount: ${total_amount}")
            return True
        else:
            print("Card details missing. Payment verification failed.")
            return False
