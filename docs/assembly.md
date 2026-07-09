# Assembly

Assembly is the PedalWorks stage where a finished bicycle actually comes together. All assembly work happens at the Portland Assembly Floor, the physical location dedicated to putting parts together into a bicycle.

PedalWorks builds two bicycle models on the Portland Assembly Floor: the City Cruiser and the Trail Blazer (see `docs/trailblazer.md`). Every City Cruiser is built from exactly the same four parts: a Frame, a Wheelset, a Drivetrain, and a Brake Set. Assembly consumes one of each of these four parts from `PartsDB` for every City Cruiser it builds — once the Scheduler has released a work order and confirmed the parts are in stock, Assembly takes them out of inventory and puts them together.

Putting a bicycle together is not free: it takes labor. Assembly posts that labor cost to the Ledger for every City Cruiser it completes, alongside the purchase, scrap, and freight costs posted by the other stages. Once assembly finishes, the resulting City Cruiser moves on to Quality for inspection before it can ship. If Quality fails a unit, it returns to Assembly for rework, and Assembly posts a second labor cost to the Ledger for that rework before the unit is inspected again.
