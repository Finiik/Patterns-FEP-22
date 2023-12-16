from pydantic import BaseModel


class CreditCard(BaseModel):
    client: str
    account_number: str
    credit_limit: float
    grace_period: int
    cvv_hash: str = None

    def give_details(self) -> dict:
        card_details = {
            "client": self.client,
            "account_number": self.account_number,
            "credit_limit": self.credit_limit,
            "grace_period": self.grace_period,
            "cvv": self.cvv_hash
        }
        return card_details

    def encrypt(self) -> None:
        self.cvv_hash = str(hash(self.cvv_hash))

    def decrypt(self, given_cvv: str) -> None:
        if hash(given_cvv) != self.cvv_hash:
            raise ValueError("The CVV's are not the same.")
