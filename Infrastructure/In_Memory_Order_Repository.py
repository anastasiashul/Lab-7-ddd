from Domain.Order import Order
from Application.Interfaces import OrderRepository

class InMemoryOrderRepository(OrderRepository):
    def __init__(self):
        self._orders : dict[str, Order] = {}

    def get_by_id(self, order_id:str):
        return self._orders.get(order_id)

    def save(self, order):
        self._orders[order.id()]=order

