# Fulfillment

Fulfillment is the theme that gets a finished bicycle from PedalWorks to the
customer who ordered it. Finished units that have cleared Quality are held
at the South Distribution Center, and it is Shipping's job to send them out
from there.

When a unit ships, Shipping reports back to Planning & Demand so the order
that started the cycle no longer counts as open. Shipping also posts the
freight cost of getting the unit from the South Distribution Center to the
customer to the Ledger — the last of the four cost kinds PedalWorks tracks.

Each shipment record ties one order's shipment back to the model it
actually shipped:

| Shipment | Model | Carrier | Freight | Ship date | Status |
|---|---|---|---|---|---|
| City Cruiser Shipment | City Cruiser | Northline Freight | $25 | 2026-02-10 | Delivered |
| Trail Blazer Shipment | Trail Blazer | Cascade Logistics | $30 | 2026-02-14 | In Transit |

The City Cruiser Shipment went out with Northline Freight on 2026-02-10 and
has already been Delivered. The Trail Blazer Shipment went out four days
later, on 2026-02-14, with Cascade Logistics, and is still In Transit. Each
shipment ships exactly one model — the City Cruiser Shipment ships the City
Cruiser, and the Trail Blazer Shipment ships the Trail Blazer.
