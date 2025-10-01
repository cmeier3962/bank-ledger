# Bank-Ledger

Quickstart

```bash
# create env (optional)
python -m venv .venv
# Windows PowerShell: .\.venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate

pip install -r requirements.txt

# run a script
$env:PYTHONPATH="src"; python scripts/smoke_test.py   # Windows PowerShell
# or
PYTHONPATH=src python scripts/smoke_test.py           # macOS/Linux

# run as module (if using __main__.py)
$env:PYTHONPATH="src"; python -m bank_ledger
