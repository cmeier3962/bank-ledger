# scripts/smoke_test.py

from datetime import datetime, UTC

from bank_ledger import Ledger, Account, Transaction


def main() -> None:
    # 1) Set up a ledger and one account
    ledger = Ledger()
    acct = Account(id="acct-001", name="Test Checking")
    ledger.add_account(acct)

    # 2) Record a deposit of 100
    tx1 = Transaction(id="tx-001", account_id="acct-001", amount=100, timestamp=datetime.now(UTC))
    ledger.record_transaction(tx1)

    # 3) Record a withdrawal of 40 (negative amount in the Transaction)
    tx2 = Transaction(id="tx-002", account_id="acct-001", amount=-40, timestamp=datetime.now(UTC))
    ledger.record_transaction(tx2)

    # 4) Inspect results
    print("Transactions recorded:", len(ledger.transactions))
    print("Last transaction amount:", ledger.transactions[-1].amount)
    print("Balance:", ledger.get_account("acct-001").balance)  # expect 60


if __name__ == "__main__":
    main()
