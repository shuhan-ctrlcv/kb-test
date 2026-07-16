# Finance

Finance is the PedalWorks theme that owns the Ledger — the one place every
other theme's spending ends up. Where Planning & Demand is the factory's
fan-out point (one decision point that drives many themes), the Ledger is
the fan-in point: many processes each post one cost to it, and Finance is
the theme responsible for that Ledger. The Ledger itself is persisted in
`LedgerDB`, the system that stores every posted entry.

Four cost kinds get posted to the Ledger, each with its own source process:

| Cost kind | Posted by |
|---|---|
| Purchase Cost | Procurement |
| Labor Cost | Assembly |
| Scrap Cost | Quality |
| Freight Cost | Shipping |

In prose: Procurement posts a Purchase Cost each time it orders parts from
a supplier. Assembly posts a Labor Cost each time it puts a unit together,
and posts another Labor Cost each time it reworks a unit that failed
Quality. Quality posts a Scrap Cost each time it runs an inspection,
whether the unit passes or fails. Shipping posts a Freight Cost each time
it ships a finished unit out. Inventory, by contrast, posts nothing to the
Ledger — it only tracks stock levels in `PartsDB` and never spends money
itself.

Each individual posting becomes its own ledger entry, tagged with the
theme it came from, the cost kind it is, and the amount:

| Ledger entry | Stage | Kind | Amount |
|---|---|---|---|
| Purchase Ledger Entry | Supply | Purchase Cost | $120 |
| Labor Ledger Entry | Production | Labor Cost | $45 |
| Scrap Ledger Entry | Production | Scrap Cost | $10 |
| Freight Ledger Entry | Fulfillment | Freight Cost | $25 |

The Purchase Ledger Entry comes out of Supply at $120, matching a single
part's unit cost. The Labor Ledger Entry and the Scrap Ledger Entry both
come out of Production — $45 for the labor and $10 for the scrap — since
Assembly and Quality are both Production processes. The Freight Ledger
Entry comes out of Fulfillment at $25. Each entry is of exactly one kind:
the Purchase Ledger Entry is of kind Purchase Cost, the Labor Ledger Entry
is of kind Labor Cost, the Scrap Ledger Entry is of kind Scrap Cost, and
the Freight Ledger Entry is of kind Freight Cost.

Because every one of these postings lands in the same `LedgerDB`, the
Ledger's running total is a complete record of everything the factory has
spent across Supply, Production, and Fulfillment for a given cycle.
