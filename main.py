from mce.domain.customer import Customer
from mce.domain.order import Order
from mce.domain.product import Product, PhysicalProduct
from mce.domain.money import Money
from mce.domain.invoice import Invoice
from mce.domain.payment import CreditCardProcessor


customer = Customer("1", "John")
payment_processor = CreditCardProcessor()
order = Order("1", customer, payment_processor)

prod = PhysicalProduct("1", "x", Money(10, "USD"), Money(2.5, "USD"))
prod1 = PhysicalProduct("2", "y", Money(20, "USD"), Money(2.5, "USD"))


order.add_product(prod, 1)
order.add_product(prod1, 2)

print("=== Order BEFORE remove ===")
invoice = Invoice(order)
print(invoice.generate_text())


order.remove_product(prod1)

print("=== Order AFTER removing 'y' ===")
invoice = Invoice(order)
print(invoice.generate_text())