# Planning & Demand — orders

Every order starts with the Customer. The Customer places an order for a
model — a City Cruiser or a Trail Blazer — and that order lands in OrderDB,
the system of record for everything PedalWorks has been asked to build.
OrderDB does not track much about an order beyond two things: which model
and quantity it's for, and whether it is still open or has already shipped.
An order stays open from the moment the Customer places it until Shipping
marks it shipped; only then does OrderDB consider it closed out.

The Planner is what turns an open order into work on the factory floor. On
each cycle, the Planner reads OrderDB for the orders the Customer has
placed and are still open, and reads PartsDB for how much of each part is
currently on hand. From those two reads it makes two decisions. First, for
each part in the catalog, if PartsDB shows the part's stock has run low, the
Planner triggers a reorder — it hands that part off to Procurement so more
gets bought in before the shelf runs dry. Second, for the order itself, the
Planner decides which model to build from the order's model field and
releases the work: a City Cruiser order goes to the Assembly line, a Trail
Blazer order goes to the Trail Blazer line. The Planner itself never touches
a wrench or a purchase order directly — it only reads OrderDB and PartsDB
and decides, then lets Procurement and Assembly do the rest.

PedalWorks tracks every customer order as its own record, from the moment
it is placed through to the shipment that closes it out. The table below is
the current state of the two orders in the system.

| Order ID | Model | Qty | Status | Date |
|---|---|---|---|---|
| ORD-1042 | City Cruiser | 20 | Shipped | 2026-02-01 |
| ORD-1077 | Trail Blazer | 15 | In Transit | 2026-02-05 |

ORD-1042 is a City Cruiser order for 20 units, placed 2026-02-01, and it has
already shipped. ORD-1077 is a Trail Blazer order for 15 units, placed a few
days later on 2026-02-05, and is still in transit rather than delivered.
