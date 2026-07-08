# Data model

This page describes the domain entities shared across every PedalWorks stage, and the three named systems that store them. The entities are plain data shapes — no behavior — and every stage module in `src/` builds, reads, or passes around one of these.

## Entities

**Part** — a component PedalWorks buys from a single supplier. Fields: `name` (its name, e.g. Frame), `supplier` (the supplier it is bought from), `lead_time_days` (days between placing an order and delivery), and `unit_cost` (cost per unit).

**Supplier** — an external company that supplies exactly one part. Fields: `name` (the supplier's name, e.g. FrameForge Ltd) and `part` (the part it supplies).

**Warehouse** — a physical location with a role in the flow. Fields: `name` (e.g. North Intake Warehouse) and `role` (its role in the flow — intake, assembly, or distribution).

**Bicycle** — the finished good. A City Cruiser is a Frame, a Wheelset, a Drivetrain, and a Brake Set. Fields: `model` (the bicycle model, e.g. City Cruiser) and `parts` (the list of part names it was built from).

**Order** — a customer order for some quantity of a bicycle model. Fields: `order_id` (a unique order identifier), `model` (the bicycle model ordered), and `qty` (the quantity ordered).

**LedgerEntry** — one cost posted to the Ledger by a stage. Fields: `stage` (which stage posted it, e.g. Procurement), `kind` (the kind of cost — purchase, labor, scrap, or freight), and `amount` (the cost amount).

## Named systems

Three named systems hold this data at runtime:

- `PartsDB` — part stock levels, keyed by part name. Read and written by Inventory, the Scheduler, and Procurement.
- `OrderDB` — customer orders. Read by the Scheduler to find open orders; updated by Shipping when an order is marked shipped.
- `LedgerDB` — the backing store for the Ledger. Every `LedgerEntry` that a stage posts is appended here, and the Ledger's running total is the sum of everything in `LedgerDB`.
