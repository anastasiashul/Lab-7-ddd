from abc import ABC, abstractmethod
from Domain.Money import Money
from Domain.Order import Order

class OrderRepository(ABC):
    @abstractmethod
    def get_by_id(self, order_id:str):
        pass
    @abstractmethod
    def save(self, order:Order): pass

class PaymentGateway(ABC):
    @abstractmethod
    def charge(self, order_id:str, money:Money):pass

