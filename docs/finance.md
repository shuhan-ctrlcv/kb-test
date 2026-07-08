# Finance

Finance is the PedalWorks stage that owns the Ledger — the one place every other stage's spending ends up. Where the Scheduler is the factory's fan-out hub (one decision point that triggers many stages), the Ledger is the fan-in hub: many stages each post one cost to it, and Finance is the stage responsible for that Ledger. The Ledger itself is persisted in `LedgerDB`, the system that stores every posted entry.

Four stages post a cost to the Ledger, one cost kind each:

| Stage | Cost kind posted |
|---|---|
| Procurement | purchase cost |
| Assembly | labor cost |
| Quality | scrap cost |
| Shipping | freight cost |

In prose: Procurement posts a purchase cost each time it orders parts from a supplier. Assembly posts a labor cost each time it puts a City Cruiser together on the Portland Assembly Floor. Quality posts a scrap cost each time it runs QC inspection, whether the bicycle passes or fails. Shipping posts a freight cost each time it ships a finished bicycle out from the South Distribution Center. Inventory, by contrast, posts nothing to the Ledger — it only tracks stock levels in `PartsDB` and never spends money itself.

Because every one of those four postings lands in the same `LedgerDB`, the Ledger's running total is a complete record of everything the factory has spent across procurement, assembly, quality, and shipping for a given cycle.
