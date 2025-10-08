from bank_ledger import Account, Ledger, Transaction
from datetime import datetime, UTC, timedelta

now = datetime.now(UTC)
l = Ledger()
l.add_account(Account("A", balance=0))
l.deposit("A", 10)  # now-ish

start = now - timedelta(seconds=5)
end = now + timedelta(seconds=5)
print([tx.amount for tx in l.transactions_between("A", start, end)])  # -> [10]
