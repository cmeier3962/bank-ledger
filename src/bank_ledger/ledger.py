from __future__ import annotations
from .transaction import Transaction
from .account import Account
from datetime import datetime, UTC
from uuid import uuid4


class Ledger:
    def __init__(self) -> None:
        self._accounts: dict[str, Account] = {}
        self.transactions: list[Transaction] = []

    def add_account(self, account: Account) -> None:
        """Register a new account; raise if the account ID already exists."""
        account_id = account.id
        if account_id in self._accounts:
            raise ValueError(f"Account '{account_id}' already exists")
        self._accounts[account_id] = account

    def get_account(self, account_id: str) -> Account | None:
        """Return the Account for this ID if present; otherwise None."""
        return self._accounts.get(account_id)

    def remove_account(self, account_id: str) -> Account | None:
        """Remove and return the account for this ID; return None if missing."""
        return self._accounts.pop(account_id, None)

    def has_account(self, account_id: str) -> bool:
        """Return True if an account with this ID exists."""
        return account_id in self._accounts

    def __contains__(self, account_id: str) -> bool:
        """Return True if an account with this ID exists."""
        return self.has_account(account_id)

    def record_transaction(self, tx: Transaction) -> None:
        """Apply a Transaction to the matching Account and record it in history.

        Positive tx.amount => deposit; negative => withdraw; zero => error.
        """
        if not self.has_account(tx.account_id):
            raise ValueError(f"Account '{tx.account_id}' does not exist")

        account = self.get_account(tx.account_id)
        assert account is not None  # for type checkers; guarded above

        if tx.amount > 0:
            account.deposit(tx.amount)
        elif tx.amount < 0:
            account.withdraw(abs(tx.amount))
        else:
            raise ValueError("Transaction amount cannot be zero")

        self.transactions.append(tx)
    
    def deposit(self, account_id: str, amount: int | float) -> Transaction:
        """
        Creates a transaction and passes it into the record_transaction method which:
        - Verifies if an account_id has an active account
        - Determines whether to deposit or withdraw the amount by its value
        - Adds the transaction to the transaction list
        """
        if amount <= 0:
            raise ValueError("Amount cannot be zero or negative")
        
        trxn = Transaction(tx_id=str(uuid4()), account_id=account_id, amount=amount, timestamp=datetime.now(UTC))
        self.record_transaction(trxn)
        
        return trxn
        
    def withdraw(self, account_id: str, amount: int | float) -> Transaction:
        """
        Creates a transaction and converts amount to negative before passes it into the record_transaction method which:
        - Verifies if an account_id has an active account
        - Determines whether to deposit or withdraw the amount by its value
        - Adds the transaction to the transaction list
        """ 
        if amount <= 0:
            raise ValueError("Amount cannot be zero or negative")
        
        trxn = Transaction(tx_id=str(uuid4()), account_id=account_id, amount=-amount, timestamp=datetime.now(UTC))
        self.record_transaction(trxn)
        
        return trxn
    
    def balance(self, account_id: str) -> int | float:
        """Returns account balance if the account exists"""
        account = self.get_account(account_id)
        if account is None:
            raise ValueError(f"Account {account_id} does not exist")
        
        return account.balance
