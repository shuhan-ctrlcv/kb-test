"""Inventory stage — tracks part stock levels in PartsDB.

Incoming parts are received at the North Intake Warehouse and recorded in
PartsDB; this module answers how much of a part is on hand and whether that
level has dropped low enough to need reordering."""
from __future__ import annotations

from database import PartsDB
from models import Part


def stock_level(parts_db: PartsDB, part: str) -> int:
    """Current on-hand quantity of ``part`` in PartsDB."""
    return parts_db.stock(part)


def low_stock(parts_db: PartsDB, part: str, threshold: int) -> bool:
    """True if ``part``'s PartsDB stock has fallen at or below ``threshold``."""
    return parts_db.stock(part) <= threshold
