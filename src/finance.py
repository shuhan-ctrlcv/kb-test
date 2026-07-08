"""Finance stage — owns the Ledger, the single place every stage posts a cost.
Persisted in LedgerDB."""
from __future__ import annotations

from database import LedgerDB
from models import LedgerEntry


def post_cost(ledger_db: LedgerDB, stage: str, kind: str, amount: float) -> None:
    """Post one cost to the Ledger on behalf of ``stage`` (e.g. purchase,
    labor, scrap, freight). Appends a LedgerEntry to LedgerDB."""
    ledger_db.append(LedgerEntry(stage=stage, kind=kind, amount=amount))
