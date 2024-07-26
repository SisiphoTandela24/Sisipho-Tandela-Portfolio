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

def create_account():
    name = name_entry.get()
    password = password_entry.get()
    if name in accounts:
        result_text.set("Account already exists.")
    else:
        accounts[name] = BankAccount(name, password)
        result_text.set("Account created successfully.")

def login():
    name = name_entry.get()
    password = password_entry.get()
    if name in accounts and accounts[name].password == password:
        account = accounts[name]
        result_text.set(f"Welcome back, {name}!")
        check_balance_button.config(command=account.check_balance)
        deposit_button.config(command=lambda: account.deposit(float(amount_entry.get())))
        withdraw_button.config(command=lambda: account.withdraw(float(amount_entry.get())))
        transfer_button.config(command=lambda: account.transfer(transfer_target_entry.get(), float(amount_entry.get())))
        statement_button.config(command=account.get_statement)
    else:
        result_text.set("Account not found or incorrect password.")

def generate_random_password():
    password = BankAccount.generate_password()
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    messagebox.showinfo("Generated Password", f"Your generated password is:\n{password}")

accounts = {}

# Create the main window
root = tk.Tk()
root.title("B Bank")

# Create widgets
name_label = tk.Label(root, text="Enter your name:")
name_label.grid(row=0, column=0, padx=10, pady=10)

name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=10)

password_label = tk.Label(root, text="Enter your password:")
password_label.grid(row=1, column=0, padx=10, pady=10)

password_entry = tk.Entry(root, show='*')
password_entry.grid(row=1, column=1, padx=10, pady=10)

generate_password_button = tk.Button(root, text="Generate Password", command=generate_random_password)
generate_password_button.grid(row=1, column=2, padx=10, pady=10)

create_account_button = tk.Button(root, text="Create Account", command=create_account)
create_account_button.grid(row=2, column=0, columnspan=3, pady=10)

login_button = tk.Button(root, text="Login", command=login)
login_button.grid(row=3, column=0, columnspan=3, pady=10)

check_balance_button = tk.Button(root, text="Check Balance")
check_balance_button.grid(row=4, column=0, columnspan=3, pady=10)

amount_label = tk.Label(root, text="Enter amount:")
amount_label.grid(row=5, column=0, padx=10, pady=10)

amount_entry = tk.Entry(root)
amount_entry.grid(row=5, column=1, padx=10, pady=10)

deposit_button = tk.Button(root, text="Deposit")
deposit_button.grid(row=6, column=0, padx=10, pady=10)

withdraw_button = tk.Button(root, text="Withdraw")
withdraw_button.grid(row=6, column=1, padx=10, pady=10)

transfer_target_label = tk.Label(root, text="Transfer to (name):")
transfer_target_label.grid(row=7, column=0, padx=10, pady=10)

transfer_target_entry = tk.Entry(root)
transfer_target_entry.grid(row=7, column=1, padx=10, pady=10)

transfer_button = tk.Button(root, text="Transfer")
transfer_button.grid(row=8, column=0, columnspan=3, pady=10)

statement_button = tk.Button(root, text="Bank Statement")
statement_button.grid(row=9, column=0, columnspan=3, pady=10)

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, wraplength=400)
result_label.grid(row=10, column=0, columnspan=3, pady=10)

# Start the GUI event loop
root.mainloop()
  

