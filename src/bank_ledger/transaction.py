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
