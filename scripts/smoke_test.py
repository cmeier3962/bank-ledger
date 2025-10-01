from datetime import datetime, UTC
from bank_ledger import Ledger, Account, Transaction

ledger = Ledger()
acct = Account(id="acct-001", name="Checking")
ledger.add_account(acct)

# Deposit 100
t1 = Transaction(tx_id="tx-001", account_id="acct-001", amount=100, timestamp=datetime.now(UTC))
ledger.record_transaction(t1)

# Withdraw 40
t2 = Transaction(tx_id="tx-002", account_id="acct-001", amount=-40, timestamp=datetime.now(UTC))
ledger.record_transaction(t2)

print("Balance:", ledger.get_account("acct-001").balance)  # -> 60
