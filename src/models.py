"""Domain data model for the PedalWorks bicycle factory.

Plain dataclasses shared by every stage module. No behavior — just the shapes
of the things that flow through the factory: parts, suppliers, warehouses,
the bicycle we build, customer orders, and one ledger entry."""
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
class Supplier:
    """An external company that supplies exactly one part."""
    name: str
    part: str


@dataclass
class Warehouse:
    """A physical location with a role in the flow (intake / assembly / distribution)."""
    name: str
    role: str


@dataclass
class Bicycle:
    """The finished good. A City Cruiser is a Frame + Wheelset + Drivetrain + Brake Set."""
    model: str
    parts: list[str] = field(default_factory=list)


@dataclass
class Order:
    """A customer order for some quantity of a bicycle model."""
    order_id: str
    model: str
    qty: int


@dataclass
class LedgerEntry:
    """One cost posted to the Ledger by a stage (kind = purchase/labor/scrap/freight)."""
    stage: str
    kind: str
    amount: float
