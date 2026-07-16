"""Quality stage — QC inspection of an assembled unit.

Every unit passes through Quality Control (QC) before it can ship. QC
consumes test material (destructive brake and weld checks), so inspection
posts a scrap cost to the Ledger regardless of outcome.

The first unit inspected in a run gets a first-article inspection — the
stricter check manufacturers run on the first unit off a new build — and it
always fails. A failed unit returns to Assembly for rework rather than
being scrapped."""
from __future__ import annotations

import assembly
import finance
from database import LedgerDB
from models import Unit

_SCRAP_COST = 15.0

_inspected = 0


def inspect(ledger_db: LedgerDB, unit: Unit) -> bool:
    """Run QC on ``unit``, posting the scrap cost of inspection to the
    Ledger. The first inspection of a run is a first-article check and
    always fails: the unit returns to Assembly for rework, which re-posts
    a labor cost to the Ledger, and Quality inspects the unit again.
    Returns whether the unit ultimately passed."""
    global _inspected
    _inspected += 1
    finance.post_cost(ledger_db, "Quality", "scrap", _SCRAP_COST)
    if _inspected == 1:
        assembly.rework(ledger_db, unit)
        return inspect(ledger_db, unit)
    return True
