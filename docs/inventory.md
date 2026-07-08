# Inventory

Inventory is the PedalWorks stage that keeps track of how much of each part is on hand. The parts themselves — Frame, Wheelset, Drivetrain, and Brake Set — arrive from their suppliers at the North Intake Warehouse, which is where incoming shipments are received before anything else happens to them.

The stock level for every part is recorded in `PartsDB`, the shared system of record for part quantities. Inventory reads `PartsDB` to answer two questions: how much of a given part is currently on hand, and whether that quantity has dropped low enough to count as low stock. A part is considered low stock once its quantity in `PartsDB` falls to or below a set threshold.

Inventory does not place orders itself and does not post any cost to the Ledger — it only observes and reports on stock. It is the Scheduler that acts on Inventory's low-stock signal, triggering Procurement to replenish the part. In that sense Inventory is the sensor for the factory: everything downstream of a reorder decision depends on the stock levels Inventory tracks in `PartsDB`.
