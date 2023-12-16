# payment_subs.py (Bookstore Payment)
class BookPayment:
    def __init__(self):
        self.card_details = {}

    def add_card_details(self, credit_card_number: str, expiration_date: str, cvv: str):
        self.card_details = {
            'credit_card_number': credit_card_number,
            'expiration_date': expiration_date,
            'cvv': hash(cvv)
        }
        print("Credit card details added successfully.")

    def verify_payment(self, total_amount: float):
        if self.card_details:
            print(f"Payment verified for total amount: ${total_amount}")
            return True
        else:
            print("Credit card details missing. Payment verification failed.")
            return False


class Payment:
    def add_card_details(self, credit_card_number, expiration_date, cvv):
        pass

    def verify_payment(self, total_amount):
        pass
