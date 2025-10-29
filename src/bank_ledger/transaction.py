from __future__ import annotations

from datetime import datetime

# If you prefer, you can import the real datetime type later and
# change the annotation to `datetime` instead of a string.
class Transaction:
    """Represent a single ledger transaction for an account."""
    def __init__(
        self,
        tx_id: str,
        account_id: str,
        amount: int | float,
        timestamp: datetime,
    ) -> None:
        self.tx_id = tx_id
        self.account_id = account_id
        self.amount = amount
        self.timestamp = timestamp
        
    def to_dict(self) -> dict:
        pass
        
    def __repr__(self) -> str:
        return f"Transaction(tx_id={self.tx_id!r}, account_id={self.account_id!r}, amount={self.amount}, timestamp={self.timestamp.isoformat()!r})"
        