import tkinter as tk
from tkinter import messagebox
import random
import string

class BankAccount:
    def __init__(self, name, password, balance=0):
        self.name = name
        self.password = password
        self.balance = balance
        self.statement = []

    @staticmethod
    def generate_password(length=12):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))
        return password

    def deposit(self, amount):
        self.balance += amount
        self.statement.append(f"Deposited R{amount}")
        result_text.set(f"Deposited R{amount}. New balance: R{self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            result_text.set("Insufficient funds.")
            self.statement.append("Failed withdrawal attempt due to insufficient funds.")
        else:
            self.balance -= amount
            self.statement.append(f"Withdrew R{amount}.")
            result_text.set(f"Withdrew R{amount}. New balance: R{self.balance}.")

    def check_balance(self):
        result_text.set(f"Current balance: R{self.balance}")

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
            self.statement.append(f"Transferred R{amount} to {target_name}.")
            target_account.statement.append(f"Received R{amount} from {self.name}.")
            result_text.set(f"Transferred R{amount} to {target_name}. New balance: R{self.balance}")

    def get_statement(self):
        statement_str = "\n".join(self.statement)
        result_text.set(f"Bank statement for {self.name}:\n{statement_str}")

def show_create_account_window():
    create_account_window = tk.Toplevel(root)
    create_account_window.title("Create Account")

    tk.Label(create_account_window, text="Enter your name:").grid(row=0, column=0, padx=10, pady=10)
    name_entry = tk.Entry(create_account_window)
    name_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(create_account_window, text="Enter your password:").grid(row=1, column=0, padx=10, pady=10)
    password_entry = tk.Entry(create_account_window, show='*')
    password_entry.grid(row=1, column=1, padx=10, pady=10)

    def create_account():
        name = name_entry.get()
        password = password_entry.get()
        if name in accounts:
            result_text.set("Account already exists.")
        else:
            accounts[name] = BankAccount(name, password)
            result_text.set("Account created successfully.")
            create_account_window.destroy()

    tk.Button(create_account_window, text="Create Account", command=create_account).grid(row=2, column=0, columnspan=2, pady=10)

def show_login_window():
    login_window = tk.Toplevel(root)
    login_window.title("Login")

    tk.Label(login_window, text="Enter your name:").grid(row=0, column=0, padx=10, pady=10)
    name_entry = tk.Entry(login_window)
    name_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(login_window, text="Enter your password:").grid(row=1, column=0, padx=10, pady=10)
    password_entry = tk.Entry(login_window, show='*')
    password_entry.grid(row=1, column=1, padx=10, pady=10)

    def login():
        name = name_entry.get()
        password = password_entry.get()
        if name in accounts and accounts[name].password == password:
            login_window.destroy()
            show_banking_functions_window(name)
        else:
            result_text.set("Account not found or incorrect password.")

    tk.Button(login_window, text="Login", command=login).grid(row=2, column=0, columnspan=2, pady=10)

def show_banking_functions_window(name):
    banking_window = tk.Toplevel(root)
    banking_window.title("Banking Functions")

    account = accounts[name]

    def deposit_amount():
        try:
            amount = float(amount_entry.get())
            account.deposit(amount)
        except ValueError:
            result_text.set("Invalid amount entered.")

    def withdraw_amount():
        try:
            amount = float(amount_entry.get())
            account.withdraw(amount)
        except ValueError:
            result_text.set("Invalid amount entered.")

    def transfer_amount():
        try:
            amount = float(amount_entry.get())
            target_name = transfer_target_entry.get()
            account.transfer(target_name, amount)
        except ValueError:
            result_text.set("Invalid amount entered.")

    def logout():
        banking_window.destroy()
        result_text.set("Logged out successfully.")

    tk.Button(banking_window, text="Check Balance", command=account.check_balance).grid(row=0, column=0, columnspan=2, pady=10)

    tk.Label(banking_window, text="Enter amount:").grid(row=1, column=0, padx=10, pady=10)
    amount_entry = tk.Entry(banking_window)
    amount_entry.grid(row=1, column=1, padx=10, pady=10)

    tk.Button(banking_window, text="Deposit", command=deposit_amount).grid(row=2, column=0, padx=10, pady=10)
    tk.Button(banking_window, text="Withdraw", command=withdraw_amount).grid(row=2, column=1, padx=10, pady=10)

    tk.Label(banking_window, text="Transfer to (name):").grid(row=3, column=0, padx=10, pady=10)
    transfer_target_entry = tk.Entry(banking_window)
    transfer_target_entry.grid(row=3, column=1, padx=10, pady=10)

    tk.Button(banking_window, text="Transfer", command=transfer_amount).grid(row=4, column=0, columnspan=2, pady=10)
    tk.Button(banking_window, text="Bank Statement", command=account.get_statement).grid(row=5, column=0, columnspan=2, pady=10)

    tk.Button(banking_window, text="Logout", command=logout).grid(row=6, column=0, columnspan=2, pady=10)

    tk.Label(banking_window, textvariable=result_text, wraplength=400).grid(row=7, column=0, columnspan=2, pady=10)

def generate_random_password():
    password = BankAccount.generate_password()
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    messagebox.showinfo("Generated Password", f"Your generated password is:\n{password}")

accounts = {}

# Create the main window
root = tk.Tk()
root.title("B Bank")

# Welcome Page
tk.Label(root, text="Welcome to B Bank").grid(row=0, column=0, columnspan=2, pady=10)

tk.Button(root, text="Create Account", command=show_create_account_window).grid(row=1, column=0, padx=10, pady=10)
tk.Button(root, text="Login", command=show_login_window).grid(row=1, column=1, padx=10, pady=10)

result_text = tk.StringVar()

# Start the GUI event loop
root.mainloop()

