# Data model

This page describes the domain entities shared across every PedalWorks
theme, and the three named systems that store them. The entities are plain
data shapes — no behavior — and every module in `src/` builds, reads, or
passes around one of these.

## Entities

**Part** — a component PedalWorks buys from a single supplier. Fields:
`name` (its name, e.g. Frame), `material` (what it is made of, e.g.
Aluminium), `supplier` (the supplier it is bought from), `lead_time_days`
(days between placing an order and delivery), and `unit_cost` (cost per
unit).

**Supplier** — an external company that supplies exactly one part. Fields:
`name` (the supplier's name, e.g. Frames Ltd), `region` (the region it
operates out of), and `part` (the part it supplies).

**Location** — a physical place with a role in the flow. Fields: `name`
(e.g. North Intake Warehouse or South Distribution Center) and `role` (its
role in the flow — intake or distribution).

**Order** — a customer order for some quantity of a model. Fields:
`order_id` (a unique order identifier, e.g. ORD-1042), `model` (the model
ordered), `qty` (the quantity ordered), `status` (its current status, e.g.
Shipped or In Transit), and `date` (the date it was placed).

**LedgerEntry** — one cost posted to the Ledger by a process. Fields:
`stage` (the theme the posting came from, e.g. Supply), `kind` (the kind of
cost it is — Purchase Cost, Labor Cost, Scrap Cost, or Freight Cost), and
`amount` (the cost amount).

## Named systems

Three named systems hold this data at runtime:

- `PartsDB` — part stock levels, keyed by part name. Read and written by
  Inventory, the Planner, and Procurement.
- `OrderDB` — customer orders. Read by the Planner to find open orders;
  updated by Shipping when an order is marked shipped.
- `LedgerDB` — the backing store for the Ledger. Every ledger entry any
  process posts is stored here, and the Ledger's running total is the sum
  of everything `LedgerDB` holds.

`LedgerDB` is the one of the three that Finance itself owns: the Ledger
stores its running total in `LedgerDB`, the same way `PartsDB` backs
Inventory and `OrderDB` backs Planning & Demand.
