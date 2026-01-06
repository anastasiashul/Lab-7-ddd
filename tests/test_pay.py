import pytest
from Application.Pay_Order_Use_Case import PayOrderUseCase
from Domain.Money import Money
from Domain.Order import Order, OrderLine, OrderStatus
from Infrastructure.Fake_Payment_Gateway import FakePaymentGateway
from Infrastructure.In_Memory_Order_Repository import InMemoryOrderRepository


def create_order(order_id="0001"):
    order=Order(order_id)
    order.add_product(OrderLine("pr_0001", 1, Money(70)))
    order.add_product(OrderLine("pr_0002", 2, Money(100)))
    return order

def test_success_payment():
    order=create_order()
    repository = InMemoryOrderRepository()
    payment_gateway = FakePaymentGateway()
    use_case = PayOrderUseCase(repository, payment_gateway)
    repository.save(order)
    res=use_case.do(order.id())

    assert res.success is True, f"Expected success=True, got {res.message}"
    assert order.status() == OrderStatus.PAID
    assert payment_gateway.charges()[0][1].amount == 270
    
def test_empty_order():
    repository = InMemoryOrderRepository()
    payment_gateway = FakePaymentGateway()
    use_case = PayOrderUseCase(repository, payment_gateway)
    order=Order("0002")
    repository.save(order)
    result = use_case.do("0002")
    assert result.success is False
    assert result.message == "Cannot pay empty order"

def test_pay_twice():
    repository = InMemoryOrderRepository()
    payment_gateway = FakePaymentGateway()
    use_case = PayOrderUseCase(repository, payment_gateway)
    order=create_order("0003")
    repository.save(order)

    use_case.do("0003")
    result = use_case.do("0003")
        
    assert result.success is False
    assert result.message == "Order is already paid"

def test_on_change():
    repository = InMemoryOrderRepository()
    payment_gateway = FakePaymentGateway()
    use_case = PayOrderUseCase(repository, payment_gateway)

    order=create_order("0004")
    repository.save(order)
    use_case.do("0004")
    paid_order=repository.get_by_id("0004")
    with pytest.raises(ValueError, match="Cannot modify paid order"):
        paid_order.add_product(OrderLine("pr_0003", 1, Money(50)))
        
    with pytest.raises(ValueError, match="Cannot modify paid order"):
        paid_order.delete_line("pr_0002")

def test_calculate_total():
    repository = InMemoryOrderRepository()
    payment_gateway = FakePaymentGateway()
    use_case = PayOrderUseCase(repository, payment_gateway)

    order=create_order("0005")
    assert order.total()==Money(270)
    order.add_product(OrderLine("pr_0006", 2, Money(10)))
    assert order.total()==Money(290)
