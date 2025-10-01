# bank-ledger

A minimal Python package for a simple bank ledger with `Account`, `Transaction`, and `Ledger`.

- No CI, no hooks — just code you can run locally.
- Library code lives in `src/bank_ledger/`.
- Handy scripts live in `scripts/`.
- Installed in **editable mode** automatically via `requirements.txt`.

## Requirements

- Python 3.11+ (3.12/3.13 OK)

## Setup (one-time per machine)

```bash
# from the repo root
python -m venv .venv
. .\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
