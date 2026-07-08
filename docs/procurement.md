# Procurement

Procurement is the PedalWorks stage that keeps the factory supplied with raw parts. Each of the four parts that make up a City Cruiser comes from exactly one outside supplier, and each supplier has a fixed lead time — the number of days between placing an order and the part arriving — and a fixed unit cost.

The four supplier relationships are fixed and do not change part to part:

| Part | Supplier | Lead time | Unit cost |
|---|---|---|---|
| Frame | FrameForge Ltd | 14 days | $120 |
| Wheelset | RollRight Co | 7 days | $85 |
| Drivetrain | GearWorks Inc | 10 days | $95 |
| Brake Set | BrakeSafe GmbH | 10 days | $40 |

In prose: the Frame is bought from FrameForge Ltd, with a 14 day lead time and a unit cost of $120. The Wheelset comes from RollRight Co, with a 7 day lead time and a unit cost of $85 — the shortest lead time of the four. The Drivetrain is supplied by GearWorks Inc, with a 10 day lead time and a unit cost of $95. The Brake Set comes from BrakeSafe GmbH, also on a 10 day lead time, at a unit cost of $40, the cheapest of the four parts.

When the Scheduler decides that a part's stock has run low, it triggers Procurement to place an order for that part with its supplier. `PartsDB`, which holds current stock levels, is read and written by Inventory, the Scheduler, and Procurement — Procurement is the one that writes the replenishment once the ordered quantity arrives. Every order Procurement places also has a cost, and Procurement posts that purchase cost to the Ledger so it is captured alongside every other stage's spending.
