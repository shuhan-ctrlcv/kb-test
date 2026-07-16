"""Shipping stage — ships finished units from the South Distribution Center.

Marks the customer order as shipped in OrderDB and posts the freight cost of
moving the unit from the South Distribution Center to the customer. The
shipment it hands back is what fulfills the order: each order is fulfilled
by exactly one shipment, for the same model the order was placed for."""
from __future__ import annotations

import finance
from database import LedgerDB, OrderDB
from models import Order, Shipment

_FREIGHT_COST = 25.0


def ship(order_db: OrderDB, ledger_db: LedgerDB, order: Order) -> Shipment:
    """Ship the unit built for ``order`` from the South Distribution Center:
    marks the order shipped in OrderDB, posts the freight cost to the
    Ledger, and returns the Shipment that fulfills the order."""
    order_db.mark_shipped(order.order_id)
    finance.post_cost(ledger_db, "Shipping", "freight", _FREIGHT_COST)
    return Shipment(order_id=order.order_id, model=order.model)
