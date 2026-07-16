"""Assembly stage — builds a City Cruiser on the Assembly Floor.

Consumes one Frame, one Wheelset, one Drivetrain, and one Brake Set from
PartsDB, posts the labor cost of putting them together, and hands back the
finished unit. Also provides rework(), which re-posts a labor cost when a
unit is sent back from Quality after failing inspection."""
from __future__ import annotations

import finance
import inventory
from database import LedgerDB, PartsDB
from models import Unit

_PARTS = ["Frame", "Wheelset", "Drivetrain", "Brake Set"]
_LABOR_COST = 60.0
_REWORK_COST = 40.0


def assemble_city_cruiser(parts_db: PartsDB, ledger_db: LedgerDB) -> Unit:
    """Assemble one City Cruiser on the Assembly Floor from a
    Frame, Wheelset, Drivetrain, and Brake Set, posting the labor cost of
    assembly to the Ledger."""
    for name in _PARTS:
        if inventory.stock_level(parts_db, name) < 1:
            raise RuntimeError(f"Assembly: insufficient stock of {name}")
        parts_db.consume(name, 1)
    finance.post_cost(ledger_db, "Assembly", "labor", _LABOR_COST)
    return Unit("City Cruiser", list(_PARTS))


def rework(ledger_db: LedgerDB, unit: Unit) -> None:
    """Send ``unit`` back through the Assembly Floor after it
    fails Quality, re-posting the labor cost of the rework to the Ledger.
    Rework corrects the existing build rather than consuming new parts."""
    finance.post_cost(ledger_db, "Assembly", "labor", _REWORK_COST)
