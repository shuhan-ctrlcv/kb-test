# Procurement

Procurement is the PedalWorks process that keeps the factory supplied with
raw parts. Every part PedalWorks builds with comes from exactly one outside
supplier, and each supplier has a fixed lead time — the number of days
between placing an order and the part arriving — and a fixed unit cost.

The supplier relationships are fixed and do not change part to part:

| Part | Material | Supplier | Lead time | Unit cost |
|---|---|---|---|---|
| Frame | Aluminium | Frames Ltd | 14 days | $120 |
| Wheelset | Alloy | Wheels Co | 7 days | $85 |
| Drivetrain | Steel | Drivetrain Co | 10 days | $95 |
| Brake Set | Steel & Rubber | Brakes Ltd | 10 days | $40 |
| Suspension Fork | Carbon Fibre | Forks Co | 12 days | $150 |

In prose: the Frame is machined from Aluminium and bought from Frames Ltd, a
supplier based in the North region, on a 14 day lead time and a unit cost of
$120 — the longest lead time of the five. The Wheelset is built from Alloy
and comes from Wheels Co, out of the East region, on a 7 day lead time at
$85 — the shortest lead time and the cheapest of the five. The Drivetrain is
Steel, supplied by Drivetrain Co out of the West region, on a 10 day lead
time at $95. The Brake Set is Steel & Rubber, supplied by Brakes Ltd out of
the South region, also on a 10 day lead time, at $40, the cheapest part
PedalWorks buys. The Suspension Fork is Carbon Fibre, supplied by Forks Co
on a 12 day lead time at $150 — the most expensive single part PedalWorks
buys, and the one part not shared between the two bicycle models.

Each of these five supplier relationships is a straight one-to-one link:
Procurement orders from Frames Ltd, Wheels Co, Drivetrain Co, Brakes Ltd,
and Forks Co, and each of those five suppliers in turn supplies exactly one
part — Frame, Wheelset, Drivetrain, Brake Set, and Suspension Fork
respectively. No supplier splits its output across two parts, and no part
is sourced from more than one supplier.

When the Planner decides that a part's stock has run low, it triggers
Procurement to place an order for that part with its supplier. `PartsDB`,
which holds current stock levels, gets the replenishment written back once
the ordered quantity arrives. Every order Procurement places also has a
cost, and Procurement posts that purchase cost to the Ledger so it is
captured alongside every other process's spending.

For how each part breaks down below the part level — the material and
sub-parts each one is made from — see `docs/bom.md`.
