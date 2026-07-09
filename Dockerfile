FROM python:3.10-slim
WORKDIR /app
COPY src/ ./src/
# Runs one full PedalWorks factory cycle end to end: the Scheduler hub reads
# PartsDB + OrderDB, triggers Procurement, and releases Assembly work; every
# stage -- Procurement, Assembly, Quality, and Shipping -- posts its cost to
# the Ledger, backed by LedgerDB.
CMD ["python", "src/scheduler.py"]
