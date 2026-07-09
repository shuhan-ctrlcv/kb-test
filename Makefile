.PHONY: run test lint

# Executes one full PedalWorks factory cycle: Scheduler -> Procurement ->
# Inventory -> Assembly -> Quality -> Shipping, with every stage posting
# its cost to the Ledger.
run:
	python src/scheduler.py

test:
	pytest eval/

lint:
	python -m pyflakes src/
