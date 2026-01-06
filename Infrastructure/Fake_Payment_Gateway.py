from Application.Interfaces import PaymentGateway
from Domain.Money import Money

class FakePaymentGateway(PaymentGateway):
    def __init__(self, success=True):
        self._success=success
        self._charges=[]

    def charge(self, order_id:str, money:Money):
        self._charges.append((order_id, money))
        return self._success

    def charges(self): return self._charges.copy()

