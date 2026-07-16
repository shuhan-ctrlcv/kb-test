"""Domain data model for PedalWorks.

Plain dataclasses shared by every stage module. No behavior — just the shapes
of the things that flow through the factory: parts, the finished unit we
build, customer orders, the shipment that closes one out, and one ledger
entry."""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Part:
    """A component PedalWorks buys from a single supplier."""
    name: str
    supplier: str
    lead_time_days: int
    unit_cost: float


@dataclass
class Unit:
    """One finished item coming off the line — a City Cruiser or a Trail
    Blazer, built from the parts listed in ``parts``."""
    model: str
    parts: list[str] = field(default_factory=list)


@dataclass
class Order:
    """A customer order for some quantity of a model."""
    order_id: str
    model: str
    qty: int


@dataclass
class Shipment:
    """The shipment that fulfills one customer order once its unit has
    cleared Quality and gone out from the South Distribution Center."""
    order_id: str
    model: str


@dataclass
class LedgerEntry:
    """One cost posted to the Ledger by a stage (kind = purchase/labor/scrap/freight)."""
    stage: str
    kind: str
    amount: float
