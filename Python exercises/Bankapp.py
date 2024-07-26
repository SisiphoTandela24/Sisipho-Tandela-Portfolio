import tkinter as tk


class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.statement = []

    def deposit(self, amount):
        self.balance += amount
        self.statement.append(f"Deposited {amount} rands.")
        result_text.set(f"Deposited {amount} rands. New balance: {self.balance} rands.")

    def withdraw(self, amount):
        if amount > self.balance:
            result_text.set("Insufficient funds.")
            self.statement.append("Failed withdrawal attempt due to insufficient funds.")
        else:
            self.balance -= amount
            self.statement.append(f"Withdrew {amount} rands.")
            result_text.set(f"Withdrew {amount} rands. New balance: {self.balance} rands.")

    def check_balance(self):
        result_text.set(f"Current balance: {self.balance} rands.")

    def transfer(self, target_name, amount):
        if target_name not in accounts:
            result_text.set("Target account not found.")
        elif amount > self.balance:
            result_text.set("Insufficient funds.")
            self.statement.append("Failed transfer attempt due to insufficient funds.")
        else:
            target_account = accounts[target_name]
            self.balance -= amount
            target_account.balance += amount
            self.statement.append(f"Transferred {amount} rands to {target_name}.")
            target_account.statement.append(f"Received {amount} rands from {self.name}.")
            result_text.set(f"Transferred {amount} rands to {target_name}. New balance: {self.balance} rands.")

    def get_statement(self):
        statement_str = "\n".join(self.statement)
        result_text.set(f"Bank statement for {self.name}:\n{statement_str}")


def create_account():
    name = name_entry.get()
    if name in accounts:
        result_text.set("Account already exists.")
    else:
        accounts[name] = BankAccount(name)
        result_text.set("Account created successfully.")


def login():
    name = name_entry.get()
    if name in accounts:
        account = accounts[name]
        result_text.set(f"Welcome back, {name}!")
        check_balance_button.config(command=account.check_balance)
        deposit_button.config(command=lambda: account.deposit(float(amount_entry.get())))
        withdraw_button.config(command=lambda: account.withdraw(float(amount_entry.get())))
        transfer_button.config(command=lambda: account.transfer(transfer_target_entry.get(), float(amount_entry.get())))
        statement_button.config(command=account.get_statement)
    else:
        result_text.set("Account not found. Please create an account first.")


accounts = {}

# Create the main window
root = tk.Tk()
root.title("B Bank")

# Create widgets
name_label = tk.Label(root, text="Enter your name:")
name_label.grid(row=0, column=0)

name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

create_account_button = tk.Button(root, text="Create Account", command=create_account)
create_account_button.grid(row=1, column=0, columnspan=2)

login_button = tk.Button(root, text="Login", command=login)
login_button.grid(row=2, column=0, columnspan=2)

check_balance_button = tk.Button(root, text="Check Balance")
check_balance_button.grid(row=3, column=0, columnspan=2)

amount_label = tk.Label(root, text="Enter amount:")
amount_label.grid(row=4, column=0)

amount_entry = tk.Entry(root)
amount_entry.grid(row=4, column=1)

deposit_button = tk.Button(root, text="Deposit")
deposit_button.grid(row=5, column=0)

withdraw_button = tk.Button(root, text="Withdraw")
withdraw_button.grid(row=5, column=1)

transfer_target_label = tk.Label(root, text="Transfer to (name):")
transfer_target_label.grid(row=6, column=0)

transfer_target_entry = tk.Entry(root)
transfer_target_entry.grid(row=6, column=1)

transfer_button = tk.Button(root, text="Transfer")
transfer_button.grid(row=7, column=0, columnspan=2)

statement_button = tk.Button(root, text="Bank Statement")
statement_button.grid(row=8, column=0, columnspan=2)

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, wraplength=400)
result_label.grid(row=9, column=0, columnspan=2)

# Start the GUI event loop
root.mainloop()

