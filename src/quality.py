"""Quality stage — QC inspection of an assembled bicycle.

Every bicycle passes through Quality Control (QC) before it can ship. QC
consumes test material (destructive brake and weld checks), so inspection
posts a scrap cost to the Ledger regardless of outcome."""
from __future__ import annotations

import finance
from models import Bicycle

_SCRAP_COST = 15.0


def inspect(ledger_db: LedgerDB, bicycle: Bicycle) -> bool:
    """Run QC on ``bicycle``, posting the scrap cost of inspection to the
    Ledger, and return whether it passed."""
    finance.post_cost(ledger_db, "Quality", "scrap", _SCRAP_COST)
    return True
