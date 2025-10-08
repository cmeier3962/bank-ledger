class LedgerError(Exception):
    pass

class AccountNotFoundError(LedgerError):
    pass

class InsufficientFundsError(LedgerError):
    pass

class InvalidAmountError(LedgerError):
    pass