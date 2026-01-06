from dataclasses import dataclass

@dataclass(frozen=True)
class Money:
    amount:float
    currency: str= "RUB"

    def __post_init__(self):
        if self.amount < 0:
            raise ValueError("Amount cannot be < 0")

    def __add__(self, val: "Money"):
        if self.currency != val.currency:
            raise ValueError("Cannot add money with different currencies")
        return Money(amount=self.amount + val.amount, currency=self.currency)

    def __eq__(self, val):
        if not isinstance(val, Money):
            return False
        return self.amount == val.amount and self.currency == val.currency




    








