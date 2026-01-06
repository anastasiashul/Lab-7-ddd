from typing import List
from Domain.Money import Money
from Domain.OrderLine import OrderLine
from Domain.OrderStatus import OrderStatus

class Order:
    def __init__(self, order_id: str, lines: List[OrderLine] = None):
        self._id = order_id
        self._products: List[OrderLine] = lines if lines else []
        self._status = OrderStatus.PENDING

    def id(self): return self._id

    def status(self): return self._status

    def lines(self):
        return self._products.copy()

    def total(self):
        if not self._products:
            return Money(0)
        total = self._products[0].total()
        for pr in self._products[1:]:
            total = total + pr.total()
        return total

    def add_product(self, product: OrderLine):
        if self._status == OrderStatus.PAID:
            raise ValueError("Cannot modify paid order")
        self._products.append(product)

    def delete_line(self, product_id: str):
        if self._status == OrderStatus.PAID:
            raise ValueError("Cannot modify paid order")
        self._products = [product for product in self._products if product.product_id != product_id]

    def pay(self):
        if self._status == OrderStatus.PAID:
            raise ValueError("Order is already paid")
        if not self._products:
            raise ValueError("Cannot pay empty order")
        self._status = OrderStatus.PAID
