from dataclasses import dataclass
from Domain.Money import Money

@dataclass
class OrderLine:
    product_id: str
    quantity: int
    price: Money

    def __post_init__(self):
        if self.quantity <= 0:
            raise ValueError("Quantity must be > 0")
        if self.price.amount <= 0:
            raise ValueError("Price must be > 0")

    def total(self):
        return Money(amount=self.price.amount*self.quantity,currency= self.price.currency)



