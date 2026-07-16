"""Planner — the production hub. Reads OrderDB for orders the Customer has
placed and PartsDB for current stock; triggers Procurement when a part is
low; releases the work order to Assembly (City Cruiser) or the Trail
Blazer line depending on the order's model; runs Quality, which reworks a
failed unit back through Assembly before passing it; then hands the
finished unit to Shipping, whose shipment fulfills the order."""
from __future__ import annotations

import assembly
import inventory
import procurement
import quality
import shipping
import trailblazer
from database import LedgerDB, OrderDB, PartsDB
from models import Order, Part

_LOW_STOCK_THRESHOLD = 1

_CATALOG = [
    Part("Frame", "Frames Ltd", 14, 120.0),
    Part("Wheelset", "Wheels Co", 7, 85.0),
    Part("Drivetrain", "Drivetrain Co", 10, 95.0),
    Part("Brake Set", "Brakes Ltd", 10, 40.0),
    Part("Suspension Fork", "Forks Co", 12, 150.0),
]


def _orders_placed_by_customer() -> list[Order]:
    """The orders waiting in OrderDB, each one placed by the Customer."""
    return [
        Order("ORD-2001", "City Cruiser", 1),
        Order("ORD-2002", "City Cruiser", 1),
        Order("ORD-2003", "Trail Blazer", 1),
    ]


def run_cycle() -> None:
    """Run one PedalWorks factory cycle: for every open order in OrderDB,
    top up PartsDB via Procurement when stock is low, release the work
    order to Assembly (City Cruiser) or the Trail Blazer line, run Quality
    on the result, then ship the fulfilling shipment out through Shipping."""
    parts_db = PartsDB()
    order_db = OrderDB(_orders_placed_by_customer())
    ledger_db = LedgerDB()

    for order in order_db.open_orders():
        for part in _CATALOG:
            if inventory.low_stock(parts_db, part.name, _LOW_STOCK_THRESHOLD):
                procurement.order_part(parts_db, ledger_db, part)
        if order.model == "Trail Blazer":
            unit = trailblazer.assemble_trail_blazer(parts_db, ledger_db)
        else:
            unit = assembly.assemble_city_cruiser(parts_db, ledger_db)
        passed = quality.inspect(ledger_db, unit)
        shipment = shipping.ship(order_db, ledger_db, order)
        print(f"{order.order_id}: built a {unit.model} from {unit.parts} "
              f"(QC passed: {passed}), fulfilled by shipment for {shipment.model}")

    print(f"Cycle complete. Ledger total: ${ledger_db.total():.2f}")


if __name__ == "__main__":
    run_cycle()
