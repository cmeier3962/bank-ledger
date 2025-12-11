# src/bank_ledger/gui.py
from __future__ import annotations

import json
from pathlib import Path
from tkinter import Tk, Listbox, END, BOTH, LEFT, RIGHT, Y, messagebox, simpledialog
from tkinter import ttk

from . import Ledger, Account
from .errors import AccountNotFoundError, InvalidAmountError, InsufficientFundsError

DATA_PATH = Path("ledger.json")


class LedgerApp:
    def __init__(self, root: Tk) -> None:
        self.root = root
        self.root.title("Bank Ledger")

        # Model
        self.ledger = Ledger()
        if DATA_PATH.exists():
            try:
                self.ledger = Ledger.load(DATA_PATH)
            except Exception:
                # best-effort; we’ll show errors on manual load
                pass

        # --- Layout ---
        # Left: accounts list
        left = ttk.Frame(root, padding=8)
        left.pack(side=LEFT, fill=Y)

        ttk.Label(left, text="Accounts").pack(anchor="w")
        self.accounts_list = Listbox(left, height=16, exportselection=False)
        self.accounts_list.pack(fill=Y)
        self.accounts_list.bind("<<ListboxSelect>>", self._on_select_account)

        # Right: actions + status
        right = ttk.Frame(root, padding=8)
        right.pack(side=RIGHT, fill=BOTH, expand=True)

        # Buttons
        btns = ttk.Frame(right)
        btns.pack(anchor="w", pady=(0, 8))

        ttk.Button(btns, text="New Account", command=self.create_account).grid(row=0, column=0, padx=4, pady=4, sticky="w")
        ttk.Button(btns, text="Summary", command=self.show_summary).grid(row=0, column=1, padx=4, pady=4, sticky="w")
        ttk.Button(btns, text="Save", command=self.save).grid(row=0, column=2, padx=4, pady=4, sticky="w")
        ttk.Button(btns, text="Load", command=self.load).grid(row=0, column=3, padx=4, pady=4, sticky="w")
        ttk.Button(btns, text="Quit", command=self.root.quit).grid(row=0, column=4, padx=4, pady=4, sticky="w")

        # Status area
        self.status = ttk.Label(right, text="Ready.", anchor="w")
        self.status.pack(fill="x")

        self.refresh_accounts()

    # --- UI helpers ---

    def refresh_accounts(self) -> None:
        self.accounts_list.delete(0, END)
        for acc_id in self.ledger.list_accounts():
            bal = self.ledger.balance(acc_id)
            self.accounts_list.insert(END, f"{acc_id}   —   balance: {bal}")

    def _selected_account_id(self) -> str | None:
        sel = self.accounts_list.curselection()
        if not sel:
            return None
        # Parse the ID from the line "ID   —   balance: X"
        line = self.accounts_list.get(sel[0])
        return line.split("—")[0].strip()  # left side of the em dash

    def _on_select_account(self, _event=None) -> None:
        acc_id = self._selected_account_id()
        if acc_id is None:
            self.status.config(text="Ready.")
        else:
            try:
                bal = self.ledger.balance(acc_id)
                self.status.config(text=f"Selected {acc_id!r} | balance {bal}")
            except AccountNotFoundError:
                self.status.config(text="Ready.")

    # --- Actions ---

    def create_account(self) -> None:
        acc_id = simpledialog.askstring("New Account", "Account ID:")
        if not acc_id:
            return
        name = simpledialog.askstring("New Account", "Optional name (blank for none):")
        try:
            self.ledger.add_account(Account(id=acc_id, name=name or None))
            self.refresh_accounts()
            self.status.config(text=f"Created account {acc_id!r}.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def show_summary(self) -> None:
        s = self.ledger.summary()
        lines = [
            f"Accounts: {s['accounts']}",
            f"Transactions: {s['transactions']}",
            "Balances:",
        ]
        for acc_id, bal in s["balances"].items():
            lines.append(f"  - {acc_id}: {bal}")
        lines.append(f"Total: {s['total_balance']}")
        messagebox.showinfo("Summary", "\n".join(lines))

    def save(self) -> None:
        try:
            self.ledger.save(DATA_PATH)
            self.status.config(text=f"Saved to {str(DATA_PATH)!r}.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def load(self) -> None:
        try:
            self.ledger = Ledger.load(DATA_PATH)
            self.refresh_accounts()
            self.status.config(text=f"Loaded from {str(DATA_PATH)!r}.")
        except FileNotFoundError:
            messagebox.showerror("Error", f"{DATA_PATH} not found.")
        except Exception as e:
            messagebox.showerror("Error", str(e))


def main() -> None:
    root = Tk()
    # Optional: nicer ttk theme on Windows
    try:
        style = ttk.Style()
        if "vista" in style.theme_names():
            style.theme_use("vista")
    except Exception:
        pass
    app = LedgerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
