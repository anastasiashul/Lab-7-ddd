from Application.Interfaces import OrderRepository, PaymentGateway

class PayOrderResult:
    def __init__(self, success:bool, order_id:str, message:str = ""):
        self.success = success
        self.order_id=order_id
        self.message = message

class PayOrderUseCase:
    def __init__(self, repository:OrderRepository, gateway:PaymentGateway):
        self._repository=repository
        self._gateway=gateway

    def do(self, order_id:str):
        order=self._repository.get_by_id(order_id)
        if order is None:
            return PayOrderResult(False, order_id, "Order not in storage")
        try:
            order.pay()
        except ValueError as e:
            return PayOrderResult(False, order_id, str(e))
        total=order.total()
        success=self._gateway.charge(order_id, total)

        if not success:
            return PayOrderResult(False, order_id, "payment failed")

        self._repository.save(order)
        return PayOrderResult(True, order_id, "Success")
