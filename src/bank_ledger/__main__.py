# src/bank_ledger/__main__.py
from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path

from . import Ledger, Account, Transaction  # exported from __init__
from .errors import (
    AccountNotFoundError,
    InsufficientFundsError,
    InvalidAmountError,
)

DATA_PATH = Path("ledger.json")


def prompt(msg: str) -> str:
    return input(msg).strip()


def read_amount(msg: str) -> float:
    raw = prompt(msg)
    try:
        amt = float(raw)
    except ValueError:
        raise InvalidAmountError(f"Amount must be a number, got {raw!r}")
    return amt


def print_menu() -> None:
    print(
        """
=== Bank Ledger ===
1) Create account
2) List accounts
3) Show balance
4) Deposit
5) Withdraw
6) Transfer
7) Transactions for account
8) Save
9) Load
0) Quit
"""
    )


def handle_create(ledger: Ledger) -> None:
    acc_id = prompt("New account id: ")
    name = prompt("Optional name (blank for none): ") or None
    # Start at 0; deposits/withdrawals should go through transactions
    try:
        ledger.add_account(Account(id=acc_id, name=name))
        print(f"Created account {acc_id!r}.")
    except Exception as e:
        print(f"Error: {e}")


def handle_list(ledger: Ledger) -> None:
    ids = ledger.list_accounts()
    if not ids:
        print("(no accounts)")
        return
    for i, acc_id in enumerate(ids, 1):
        print(f"{i}. {acc_id}")


def handle_balance(ledger: Ledger) -> None:
    acc_id = prompt("Account id: ")
    try:
        bal = ledger.balance(acc_id)
        print(f"Balance for {acc_id!r}: {bal}")
    except AccountNotFoundError as e:
        print(f"Error: {e}")


def handle_deposit(ledger: Ledger) -> None:
    acc_id = prompt("Account id: ")
    try:
        amt = read_amount("Amount to deposit (>0): ")
        tx = ledger.deposit(acc_id, amt)
        print(f"OK: {tx}")
    except (AccountNotFoundError, InvalidAmountError) as e:
        print(f"Error: {e}")


def handle_withdraw(ledger: Ledger) -> None:
    acc_id = prompt("Account id: ")
    try:
        amt = read_amount("Amount to withdraw (>0): ")
        tx = ledger.withdraw(acc_id, amt)
        print(f"OK: {tx}")
    except (AccountNotFoundError, InvalidAmountError, InsufficientFundsError) as e:
        print(f"Error: {e}")


def handle_transfer(ledger: Ledger) -> None:
    src = prompt("From account id: ")
    dst = prompt("To account id: ")
    try:
        amt = read_amount("Amount to transfer (>0): ")
        wtx, dtx = ledger.transfer(src, dst, amt)
        print(f"OK: {wtx}  ->  {dtx}")
    except (AccountNotFoundError, InvalidAmountError, InsufficientFundsError, ValueError) as e:
        print(f"Error: {e}")


def handle_txns_for(ledger: Ledger) -> None:
    acc_id = prompt("Account id: ")
    try:
        txns = ledger.transactions_for(acc_id)
        if not txns:
            print("(no transactions)")
            return
        for t in txns:
            print(t)
    except AccountNotFoundError as e:
        print(f"Error: {e}")


def handle_save(ledger: Ledger) -> None:
    path_str = prompt(f"Save path [{DATA_PATH}]: ") or str(DATA_PATH)
    try:
        ledger.save(path_str)
        print(f"Saved to {path_str!r}.")
    except Exception as e:
        print(f"Error: {e}")


def handle_load() -> Ledger:
    path_str = prompt(f"Load path [{DATA_PATH}]: ") or str(DATA_PATH)
    try:
        led = Ledger.load(path_str)
        print(f"Loaded from {path_str!r}.")
        return led
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"Error: {e}")
    return None  # type: ignore[return-value]


def main() -> None:
    ledger = Ledger()
    # Optional: auto-load if file exists
    if DATA_PATH.exists():
        try:
            ledger = Ledger.load(DATA_PATH)
            print(f"(Auto-loaded {DATA_PATH})")
        except Exception:
            pass

    while True:
        print_menu()
        choice = prompt("Select: ")
        if choice == "1":
            handle_create(ledger)
        elif choice == "2":
            handle_list(ledger)
        elif choice == "3":
            handle_balance(ledger)
        elif choice == "4":
            handle_deposit(ledger)
        elif choice == "5":
            handle_withdraw(ledger)
        elif choice == "6":
            handle_transfer(ledger)
        elif choice == "7":
            handle_txns_for(ledger)
        elif choice == "8":
            handle_save(ledger)
        elif choice == "9":
            new_led = handle_load()
            if new_led:
                ledger = new_led
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
