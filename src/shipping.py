"""Shipping stage — ships finished bicycles from the South Distribution
Center.

Marks the customer order as shipped in OrderDB and posts the freight cost of
moving the bicycle from the South Distribution Center to the customer."""
from __future__ import annotations

import finance
from database import LedgerDB, OrderDB
from models import Bicycle, Order

_FREIGHT_COST = 25.0


def ship(order_db: OrderDB, ledger_db: LedgerDB, bicycle: Bicycle, order: Order) -> None:
    """Ship ``bicycle`` for ``order`` from the South Distribution Center:
    marks the order shipped in OrderDB and posts the freight cost to the
    Ledger."""
    order_db.mark_shipped(order.order_id)
    finance.post_cost(ledger_db, "Shipping", "freight", _FREIGHT_COST)
