from pydantic import BaseModel
from typing import Dict


class CreditCard(BaseModel):

    client: str
    account_number: str
    credit_limit: float
    grace_period: int
    cvv_hash: str = None

    def give_details(self) -> dict:
        """Show details of a card with a dictionary"""
        card_details = {
            "client": self.client,
            "account_number": self.account_number,
            "credit_limit": self.credit_limit,
            "grace_period": self.grace_period,
            "cvv": self.cvv_hash
        }
        return card_details

    def encrypt(self) -> None:
        """Encrypt a password"""
        self.cvv_hash = str(hash(self.cvv_hash))

    def check_cvv(self, given_cvv: str) -> None:
        """Check passwords"""
        if hash(given_cvv) != self.cvv_hash:
            raise ValueError("Cvvs don't match.")


def CorporateCreditCard(cls):
    class CorporateCreditCardDecorator(cls):
        expense_tracking: Dict[str, float] = {}

        def __init__(self, *args, credit_limit: float = 10000.0, **kwargs):
            super().__init__(*args, credit_limit=credit_limit, **kwargs)

        def track_expense(self, category: str, amount: float) -> None:
            if category in self.expense_tracking:
                self.expense_tracking[category] += amount
            else:
                self.expense_tracking[category] = amount

    return CorporateCreditCardDecorator


def GoldenCreditCard(cls):
    class GoldenCreditCardDecorator(cls):
        reward_points: int = 0

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def earn_reward_points(self, points: int) -> None:
            self.reward_points += points

        def redeem_rewards(self, points_to_redeem: int) -> None:
            if points_to_redeem <= self.reward_points:
                self.reward_points -= points_to_redeem
                print(f"Redeemed {points_to_redeem} reward points.")
            else:
                print("Insufficient reward points to redeem.")

    return GoldenCreditCardDecorator


@CorporateCreditCard
class CorporateCreditCard(CreditCard):
    pass


@GoldenCreditCard
class GoldenCreditCard(CreditCard):
    pass
