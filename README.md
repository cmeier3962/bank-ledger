# bank-ledger

A minimal Python package for a simple bank ledger with `Account`, `Transaction`, and `Ledger`.

- No CI, no hooks — just code you can run locally.
- Library code lives in `src/bank_ledger/`.
- Handy scripts live in `scripts/`.

## Requirements

- Python 3.11+ (3.12 works too)
- (Optional) `make` if you want the Makefile shortcuts (Git Bash on Windows has it)

## Setup

```bash
# from repo root
python -m venv .venv

# Windows (PowerShell)
. .\.venv\Scripts\Activate.ps1
# macOS/Linux
# source .venv/bin/activate

pip install -r requirements.txt
