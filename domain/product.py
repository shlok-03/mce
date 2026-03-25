from .money import Money
from .shipping import ShippingCalculator


class Product:
    def __init__(self, product_id: str, name: str, price: Money, shipping_calculator: ShippingCalculator) -> None:
        self._id = product_id
        self._name = name
        if not isinstance(price, Money):
            raise ValueError("Price must be of type Money")
        if price.amount <= 0:
            raise ValueError("Price must be a positive value")
        self._price = price
        self._shipping_calculator = shipping_calculator

    def calculate_shipping(self) -> Money:
        return self._shipping_calculator.calculate()

    def get_total_price(self) -> Money:
        return self._price + self._shipping_calculator.calculate()

    def calculate_tax(self) -> Money:
        return Money(0, "USD")

    def __str__(self) -> str:
        return f"{self._name}\nPrice:\n---Base: {self.get_total_price()}\n---Tax: {self.calculate_tax()}"


class PhysicalProduct(Product):
    def __init__(self, product_id: str, name: str, price: Money, shipping_calculator: ShippingCalculator) -> None:
        super().__init__(product_id, name, price, shipping_calculator)

    def get_total_price(self) -> Money:
        return self._price + self.calculate_shipping()

    def calculate_tax(self) -> Money:
        return self._price * 0.15


class DigitalProduct(Product):
    pass


class SubscriptionProduct(Product):
    def __init__(self, product_id: str, name: str, price: Money, shipping_calculator: ShippingCalculator, months: int) -> None:
        super().__init__(product_id, name, price, shipping_calculator)
        self._months = months

    def get_total_price(self) -> Money:
        return self._price * self._months


class LimitedQuantityProduct(Product):
    pass