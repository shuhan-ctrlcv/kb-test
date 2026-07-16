"""In-memory fake data stores for PedalWorks: PartsDB, OrderDB, LedgerDB.
State is module-level, just enough to run one factory cycle end to end."""
from __future__ import annotations

from models import LedgerEntry, Order


class PartsDB:
    """Part stock levels, keyed by part name. Read and written by Inventory,
    the Planner, and Procurement."""
    def __init__(self) -> None:
        self._stock: dict[str, int] = {}

    def stock(self, part: str) -> int:
        return self._stock.get(part, 0)

    def receive(self, part: str, qty: int) -> None:
        self._stock[part] = self._stock.get(part, 0) + qty

    def consume(self, part: str, qty: int) -> None:
        self._stock[part] = self._stock.get(part, 0) - qty


class OrderDB:
    """Customer orders. The Planner reads open orders; Shipping marks them
    shipped once fulfilled."""
    def __init__(self, orders: list[Order] | None = None) -> None:
        self._orders = list(orders or [])
        self._shipped: set[str] = set()

    def open_orders(self) -> list[Order]:
        return [o for o in self._orders if o.order_id not in self._shipped]

    def mark_shipped(self, order_id: str) -> None:
        self._shipped.add(order_id)


class LedgerDB:
    """Backing store for the finance Ledger — an append-only list of LedgerEntry."""
    def __init__(self) -> None:
        self._entries: list[LedgerEntry] = []

    def append(self, entry: LedgerEntry) -> None:
        self._entries.append(entry)

    def total(self) -> float:
        return sum(e.amount for e in self._entries)
