# Shipping

Shipping is the last stage any PedalWorks bicycle — City Cruiser or Trail Blazer — passes through. Finished bicycles that have cleared Quality are stored at the South Distribution Center, and it is from there that Shipping sends them out to the customer who placed the order.

When a bicycle ships, Shipping updates `OrderDB` — the system that tracks customer orders — to mark that order as shipped, so it no longer counts as an open order the Scheduler needs to act on. Shipping also posts the freight cost of moving the bicycle from the South Distribution Center to the customer to the Ledger. Freight is the fourth and last of the four cost kinds posted to the Ledger, alongside the purchase cost from Procurement, the labor cost from Assembly, and the scrap cost from Quality.

Shipping is the final handoff in the PedalWorks factory flow: once it runs, the order that started the whole cycle — from the suppliers, through the North Intake Warehouse, the Scheduler, Procurement and Inventory, the Portland Assembly Floor, and Quality — is complete.
