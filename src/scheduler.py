"""Scheduler — the production hub. Reads PartsDB and OrderDB; triggers
Procurement when stock is low; releases work orders to Assembly."""
from __future__ import annotations

import assembly
import inventory
import procurement
from database import LedgerDB, OrderDB, PartsDB
from models import Order, Part

_LOW_STOCK_THRESHOLD = 1

_CATALOG = [
    Part("Frame", "FrameForge Ltd", 14, 120.0),
    Part("Wheelset", "RollRight Co", 7, 85.0),
    Part("Drivetrain", "GearWorks Inc", 10, 95.0),
    Part("Brake Set", "BrakeSafe GmbH", 10, 40.0),
]


def run_cycle() -> None:
    """Run one PedalWorks factory cycle: for every open order in OrderDB,
    top up PartsDB via Procurement when stock is low, then release the work
    order to Assembly."""
    parts_db = PartsDB()
    order_db = OrderDB([
        Order("ORD-1001", "City Cruiser", 1),
        Order("ORD-1002", "City Cruiser", 1),
    ])
    ledger_db = LedgerDB()

    for order in order_db.open_orders():
        for part in _CATALOG:
            if inventory.low_stock(parts_db, part.name, _LOW_STOCK_THRESHOLD):
                procurement.order_part(parts_db, ledger_db, part)
        bicycle = assembly.assemble_city_cruiser(parts_db, ledger_db)
        print(f"{order.order_id}: assembled a {bicycle.model} from {bicycle.parts}")

    print(f"Cycle complete. Ledger total: ${ledger_db.total():.2f}")


if __name__ == "__main__":
    run_cycle()
