from .customer import Customer
from .product import Product
from .orderline import OrderLine
from .money import Money
from .payment import PaymentProcessor


class Order:
    def __init__(self, order_id: str, customer: Customer, payment_processor: PaymentProcessor) -> None:
        self._id = order_id
        self._customer = customer
        self._lines: list[OrderLine] = []
        self._payment_processor = payment_processor

    def validate(self) -> None:
        if not self._lines:
            raise ValueError("Order must contain at least one product")

    def add_product(self, product: Product, quantity: int) -> None:
        self._lines.append(OrderLine(product, quantity))

    def remove_product(self, product: Product) -> None:
        self._lines = [line for line in self._lines if line.product != product]

    def total(self) -> Money:
        return sum(line.line_total() for line in self._lines)

    @property
    def id(self) -> str:
        return self._id

    @property
    def customer(self) -> Customer:
        return self._customer

    @property
    def lines(self) -> list[OrderLine]:
        return list(self._lines)

    def __str__(self) -> str:
        ret_val = "Order: \n"
        for line in self._lines:
            ret_val += str(line)
            ret_val += "\n"
        return ret_val