from .order import Order


class Invoice:

    def __init__(self, order: Order) -> None:
        self._order = order

    def total(self) -> str:
        return self._order.total()

    def generate_text(self) -> str:
        lines = []
        lines.append("=" * 40)
        lines.append("           INVOICE")
        lines.append("=" * 40)
        lines.append(f"Customer : {self._order.customer.name}")
        lines.append(f"Order ID : {self._order.id}")
        lines.append("-" * 40)
        lines.append("Items:")

        for line in self._order.lines:
            lines.append(str(line))

        lines.append("-" * 40)
        lines.append(f"Total    : {self._order.total()}")
        lines.append("=" * 40)

        return "\n".join(lines)