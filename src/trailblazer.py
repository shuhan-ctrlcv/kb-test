"""Trail Blazer stage — builds a Trail Blazer on the Portland Assembly Floor.

Trail Blazer is PedalWorks' second bicycle model. It reuses the Frame and
Wheelset bought for the City Cruiser and adds one new part, a Suspension
Fork, from a new supplier. Consumes one of each part from PartsDB, posts
the labor cost of assembly, and hands back the finished bicycle."""
from __future__ import annotations

import finance
import inventory
from models import Bicycle

_PARTS = ["Frame", "Wheelset", "Suspension Fork"]
_LABOR_COST = 60.0


def assemble_trail_blazer(parts_db: PartsDB, ledger_db: LedgerDB) -> Bicycle:
    """Assemble one Trail Blazer on the Portland Assembly Floor from a
    Frame, Wheelset, and Suspension Fork, posting the labor cost of
    assembly to the Ledger."""
    for name in _PARTS:
        if inventory.stock_level(parts_db, name) < 1:
            raise RuntimeError(f"Assembly: insufficient stock of {name}")
        parts_db.consume(name, 1)
    finance.post_cost(ledger_db, "Assembly", "labor", _LABOR_COST)
    return Bicycle("Trail Blazer", list(_PARTS))
