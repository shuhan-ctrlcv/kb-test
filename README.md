# kb-test — PedalWorks

`kb-test` is a hand-built "golden" test corpus for knowledge-base extraction work. It is not a real product: it is a fictional bicycle-assembly factory, **PedalWorks**, described twice — once in prose (`docs/`) and once in runnable Python (`src/`) — so that a downstream knowledge engine has a small, fully predictable graph to extract and be checked against.

## What PedalWorks does

PedalWorks builds one bicycle model, the **City Cruiser**, from four purchased parts: a Frame, a Wheelset, a Drivetrain, and a Brake Set. Each part comes from exactly one outside supplier. Parts arrive at a warehouse, get tracked in inventory, get assembled into a finished bicycle, pass a quality check, and ship out to the customer. Every stage of that journey records what it cost, and all of those costs land in one shared ledger.

The factory is organized around two hubs:
- **Scheduler** — the fan-out hub. It reads stock and order data, decides when more parts need ordering, and releases assembly work.
- **Ledger** — the fan-in hub. Every stage that spends money posts that cost to the Ledger, so it becomes the one place all factory spending converges.

Three named systems back the factory's data:
- `PartsDB` — current stock level of each part.
- `OrderDB` — customer orders, open or shipped.
- `LedgerDB` — the storage backing the Ledger; every posted cost lives here.

## Master flowchart

The diagram below traces one unit of work through the whole factory, from raw supplier to shipped bicycle. Finance and the Ledger are drawn separately at the bottom because they do not sit in the linear path — instead they receive a posting from every stage above them.

```
                     Suppliers
   (FrameForge Ltd, RollRight Co, GearWorks Inc, BrakeSafe GmbH)
                         |
                         v
          +-----------------------------+
          |   North Intake Warehouse    |   receives incoming parts
          +-----------------------------+
                         |
                         v
          +-----------------------------+
          |          Scheduler          |   reads PartsDB + OrderDB
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
          |   Portland Assembly Floor   |
          |          (Assembly)         |
          +-----------------------------+
                         |
                         v
                  +-------------+
                  |   Quality   |
                  +-------------+
                         |
                         v
          +-----------------------------+
          |  South Distribution Center  |
          |          (Shipping)         |
          +-----------------------------+

          =================================================
          |   Finance / Ledger (persisted in LedgerDB)     |
          |   touches every stage above: Procurement,      |
          |   Assembly, Quality, and Shipping each post     |
          |   a cost to it.                                |
          =================================================
```

## Repo layout

- `src/` — nine runnable Python modules (`models.py`, `database.py`, `finance.py`, `procurement.py`, `inventory.py`, `assembly.py`, `quality.py`, `shipping.py`, `scheduler.py`), one per stage plus the shared data model and fake databases. Running `python scheduler.py` executes one full factory cycle end to end.
- `docs/` — one markdown file per business stage (`procurement.md`, `inventory.md`, `assembly.md`, `quality.md`, `shipping.md`, `finance.md`) plus `data-model.md`, describing the same factory in prose.
- `eval/` — hand-written eval artifacts (`expected_structure.yaml`, `gold_qa.yaml`) used to check a later, automated extraction run against this corpus. No extraction happens in this repo.
