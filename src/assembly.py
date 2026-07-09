"""Assembly stage — builds a City Cruiser on the Portland Assembly Floor.

Consumes one Frame, one Wheelset, one Drivetrain, and one Brake Set from
PartsDB, posts the labor cost of putting them together, and hands back the
finished bicycle. Also provides rework(), which re-posts a labor cost when
a unit is sent back from Quality after failing inspection."""
from __future__ import annotations

import finance
import inventory
from models import Bicycle

_PARTS = ["Frame", "Wheelset", "Drivetrain", "Brake Set"]
_LABOR_COST = 60.0
_REWORK_COST = 40.0


def assemble_city_cruiser(parts_db: PartsDB, ledger_db: LedgerDB) -> Bicycle:
    """Assemble one City Cruiser on the Portland Assembly Floor from a
    Frame, Wheelset, Drivetrain, and Brake Set, posting the labor cost of
    assembly to the Ledger."""
    for name in _PARTS:
        if inventory.stock_level(parts_db, name) < 1:
            raise RuntimeError(f"Assembly: insufficient stock of {name}")
        parts_db.consume(name, 1)
    finance.post_cost(ledger_db, "Assembly", "labor", _LABOR_COST)
    return Bicycle("City Cruiser", list(_PARTS))


def rework(ledger_db: LedgerDB, bicycle: Bicycle) -> None:
    """Send ``bicycle`` back through the Portland Assembly Floor after it
    fails Quality, re-posting the labor cost of the rework to the Ledger.
    Rework corrects the existing build rather than consuming new parts."""
    finance.post_cost(ledger_db, "Assembly", "labor", _REWORK_COST)
