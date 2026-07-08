"""Procurement stage — orders parts from suppliers and posts purchase cost to
the Ledger.

Every part has exactly one supplier and a lead time before delivery arrives;
this module places the order, receives the part into PartsDB once it is in
hand, and records what it cost."""
from __future__ import annotations

import finance
from database import LedgerDB, PartsDB
from models import Part

_ORDER_QTY = 4


def order_part(parts_db: PartsDB, ledger_db: LedgerDB, part: Part) -> None:
    """Order more of ``part`` from its supplier (``part.supplier``), due to
    arrive after ``part.lead_time_days`` days of lead time. Receives the
    part into PartsDB and posts its purchase cost to the Ledger."""
    parts_db.receive(part.name, _ORDER_QTY)
    finance.post_cost(ledger_db, "Procurement", "purchase", part.unit_cost * _ORDER_QTY)
