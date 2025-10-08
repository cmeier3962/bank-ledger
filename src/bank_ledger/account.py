from __future__ import annotations
from .errors import InvalidAmountError, InsufficientFundsError


class Account:
    """Represent a bank account with id, optional name, and running balance."""
    def __init__(self, id: str, name: str | None = None, balance: int | float = 0) -> None:
        self.id = id
        self.name = name
        self.balance = balance

    def deposit(self, amount: int | float) -> None:
        """Deposit a positive amount into the account."""
        if amount <= 0:
            raise InvalidAmountError("Cannot deposit zero dollars or a negative amount")
        self.balance += amount

    def withdraw(self, amount: int | float) -> None:
        """Withdraw a positive amount from the account (no overdrafts)."""
        if amount <= 0:
            raise InvalidAmountError("Cannot withdraw zero dollars or a negative amount")
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds")
        self.balance -= amount
        
    def __repr__(self) -> str:
        return f"Account(id={self.id!r}, name={self.name!r}, balance={self.balance})"
