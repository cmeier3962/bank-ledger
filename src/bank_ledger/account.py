from __future__ import annotations


class Account:
    """Represent a bank account with id, optional name, and running balance."""
    def __init__(self, id: str, name: str | None = None, balance: int | float = 0) -> None:
        self.id = id
        self.name = name
        self.balance = balance

    def deposit(self, amount: int | float) -> None:
        """Deposit a positive amount into the account."""
        if amount <= 0:
            raise ValueError("Cannot deposit zero dollars or a negative amount")
        self.balance += amount

    def withdraw(self, amount: int | float) -> None:
        """Withdraw a positive amount from the account (no overdrafts)."""
        if amount <= 0:
            raise ValueError("Cannot withdraw zero dollars or a negative amount")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
