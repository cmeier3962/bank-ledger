# bank-ledger

A minimal Python package for a simple bank ledger with `Account`, `Transaction`, and `Ledger`.

- Library code lives in `src/bank_ledger/`
- Handy scripts live in `scripts/`
- Installed locally in **editable mode** via `requirements.txt` (contains `-e .`)

## Repo layout

```
bank-ledger/
├─ src/
│  └─ bank_ledger/
│     ├─ __init__.py
│     ├─ __main__.py
│     ├─ account.py
│     ├─ ledger.py
│     └─ transactions.py
├─ scripts/
│  └─ smoke_test.py
├─ .gitignore
├─ pyproject.toml
├─ requirements.txt
└─ README.md
```

## Requirements
- Python 3.11+ (3.12/3.13 OK)

## Setup

```bash
# from repo root
python -m venv .venv
```

**Windows (PowerShell):**
```powershell
. .\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

**macOS/Linux:**
```bash
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

This installs the package in **editable** mode so changes under `src/bank_ledger/` are picked up immediately.

## Quick check

Run the module:
```bash
python -m bank_ledger
```

Run the smoke script:
```bash
python scripts/smoke_test.py
```
