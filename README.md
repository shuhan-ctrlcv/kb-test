# kb-test — PedalWorks

PedalWorks is a fictional bicycle-assembly company used for testing. It is
organized around six themes — **Planning & Demand**, **Supply**,
**Inventory**, **Production**, **Fulfillment**, and **Finance** — described
both in prose (`docs/`) and in runnable Python (`src/`).

## What PedalWorks does

PedalWorks builds two models. The **City Cruiser** is built from four
purchased parts: a Frame, a Wheelset, a Drivetrain, and a Brake Set. The
**Trail Blazer** reuses the Frame and Wheelset and adds a fifth purchased
part, the Suspension Fork, in place of the Drivetrain and Brake Set. Each
part comes from exactly one outside supplier — Frames Ltd, Wheels Co,
Drivetrain Co, Brakes Ltd, and Forks Co. Parts arrive at a warehouse, get
tracked in inventory, get assembled into a finished unit, pass a quality
check, and ship out to the customer. Every stage of that journey records
what it cost, and all of those costs land in one shared ledger.

The factory is organized around two hubs:
- **Planner** — the fan-out hub. It reads OrderDB for orders the Customer
  has placed and PartsDB for current stock, decides when a part needs
  reordering, and releases assembly work.
- **Ledger** — the fan-in hub. Every stage that spends money posts that
  cost to the Ledger, so it becomes the one place all factory spending
  converges.

Three named systems back the factory's data:
- `PartsDB` — current stock level of each part.
- `OrderDB` — customer orders, open or shipped.
- `LedgerDB` — the storage backing the Ledger; every posted cost lives here.

## Master flowchart

The diagram below traces one unit of work through the whole factory, from
raw supplier to shipped unit. Finance and the Ledger are drawn separately
at the bottom because they do not sit in the linear path — instead they
receive a posting from every stage above them.

```
                     Suppliers
       (Frames Ltd, Wheels Co, Drivetrain Co, Brakes Ltd, Forks Co)
                         |
                         v
          +-----------------------------+
          |   North Intake Warehouse    |   receives incoming parts
          +-----------------------------+
                         |
                         v
          +-----------------------------+
          |           Planner           |   reads PartsDB + OrderDB
          |         (fan-out hub)       |   triggers Procurement on low stock
          +-----------------------------+   releases work to Assembly
               |                   |
               v                   v
      +---------------+   +---------------+
      |  Procurement  |   |   Inventory   |
      +---------------+   +---------------+
               |                   |
               +---------+---------+
                         v
          +-----------------------------+
          |        Assembly Floor       |<----------+
          |          (Assembly)         |           |
          +-----------------------------+           |
                         |                          |
                         v                          | rework: failed QC returns to Assembly
                  +-------------+                   |
                  |   Quality   |-------------------+
                  +-------------+
                         |
                         v
          +-----------------------------+
          |  South Distribution Center  |
          |          (Shipping)         |
          +-----------------------------+
                         |
                         v
                  fulfills the order

          =================================================
          |   Finance / Ledger (persisted in LedgerDB)     |
          |   touches every stage above: Procurement,      |
          |   Assembly, Quality, and Shipping each post     |
          |   a cost to it.                                |
          =================================================
```

## Repo layout

- `src/` — nine runnable Python modules (`models.py`, `database.py`,
  `finance.py`, `procurement.py`, `inventory.py`, `assembly.py`,
  `quality.py`, `shipping.py`, `trailblazer.py`, `planner.py`), one per
  stage (plus the Trail Blazer variant) and the shared data model and fake
  databases. Running `python planner.py` executes one full factory cycle
  end to end.
- `docs/` — one markdown file per theme (`architecture-flow.md`,
  `planning_and_demand.md`, `procurement.md`, `bom.md`, `inventory.md`,
  `production.md`, `fulfillment.md`, `finance.md`), plus `data-model.md`
  for the three backing systems. `docs/architecture-flow.md` is the
  whole-system view — start there. A few facts live outside markdown on
  purpose, as duplicates or probes in other formats:
  `docs/supplier_catalog.pdf`, `docs/quality_checklist.docx`, and
  `docs/factory_overview.pptx`.
- `data/inventory_stock.xlsx` — per-part stock records and a duplicate of
  the supplier/lead-time/cost table.
- `analysis/yield_analysis.ipynb` — the first-pass-yield calculation for a
  production run.
