# Production

Production is the PedalWorks theme where purchased parts become a finished
bicycle. It covers two processes — Assembly, where the parts are put
together, and Quality, where the assembled unit is inspected — plus the two
models that come out the other end.

## Assembly

Assembly is where a unit actually comes together, one build step at a time,
always in the same order:

1. Mount Frame
2. Attach Wheelset
3. Install Drivetrain
4. Fit Brakes
5. Final Fit

Once the Planner has released a work order and confirmed the parts are in
stock, Assembly takes them out of `PartsDB` and works through those five
steps in sequence, ending with Final Fit before the unit moves on. Putting a
unit together is not free — it takes labor, and Assembly posts that labor
cost to the Ledger for every unit it completes.

## Quality

Once Assembly finishes, the unit feeds into Quality for inspection before it
is allowed to ship. Running that inspection is not free either, even when
the unit passes: the process consumes test material, so every inspection
posts a scrap cost to the Ledger regardless of the outcome.

Not every unit clears inspection on the first attempt. A unit that fails
returns to Assembly for rework — Quality reworks it back to Assembly rather
than scrapping it — and Assembly re-posts a labor cost for the extra work
before Quality inspects it again. The exact checks Quality runs, and the
order it runs them in, are documented separately in the QC checklist.

## Products

PedalWorks builds two models, grouped together under Products: the **City
Cruiser** and the **Trail Blazer**.

The City Cruiser is built from four parts: a Frame, a Wheelset, a
Drivetrain, and a Brake Set. The Trail Blazer shares two of those three —
the Frame and the Wheelset — but swaps out the Drivetrain and Brake Set for
a Suspension Fork instead, which is the one part the two models do not have
in common. Every City Cruiser and every Trail Blazer goes through the same
five Assembly steps and the same Quality inspection regardless of which
parts it was built from.
