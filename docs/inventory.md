# Inventory

Inventory is the PedalWorks theme that keeps track of how much of each part
is on hand. The parts themselves — Frame, Wheelset, Drivetrain, Brake Set,
and Suspension Fork — arrive from their suppliers at the North Intake
Warehouse, which is where incoming shipments are received before anything
else happens to them.

The stock level for every part is recorded in `PartsDB`, the shared system
of record for part quantities. Watching that system is the job of Stock
Tracking, a sensor that monitors `PartsDB` rather than acting on it directly.
Stock Tracking flags a part as low stock the moment it is on-hand at or
below the reorder point — that is the rule it applies to every part, all the
time, without exception.

Inventory does not place orders itself and does not post any cost to the
Ledger — it only observes and reports on stock. It is the Planner that acts
on Stock Tracking's low-stock signal, triggering Procurement to replenish
the part. In that sense Stock Tracking is the sensor for the whole factory:
everything downstream of a reorder decision depends on the stock levels it
watches in `PartsDB`.
