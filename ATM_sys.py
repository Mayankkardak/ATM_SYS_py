import tkinter as tk
from tkinter import messagebox
import random
from datetime import datetime



class Account:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.transaction_history.append(f"{timestamp} - Deposited: {amount}")
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.transaction_history.append(f"{timestamp} - Withdrew: {amount}")
            return True
        return False

    def get_balance(self):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.transaction_history.append(f"{timestamp} - Checked balance: {self.balance}")
        return self.balance

    def get_transaction_history(self):
        return self.transaction_history

class ATM:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account

    def authenticate(self, account_number, pin):
        account = self.accounts.get(account_number)
        if account and account.pin == pin:
            return account
        return None
print("this line")
class ATMGUI:
    def __init__(self, root, atm):
        self.root = root
        self.atm = atm
        self.user_account = None
        self.root.title("ATM System")

        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack()

        self.create_account_widgets()

    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def create_account_widgets(self):
        self.clear_frame()

        tk.Label(self.main_frame, text="Create Account", font=('Helvetica', 16)).pack(pady=10)

        tk.Label(self.main_frame, text="Enter 4-digit PIN:").pack()
        self.pin_entry = tk.Entry(self.main_frame, show='*')
        self.pin_entry.pack()

        tk.Button(self.main_frame, text="Create Account", command=self.create_account).pack(pady=5)
        tk.Button(self.main_frame, text="Login", command=self.create_login_widgets).pack(pady=5)

    def create_account(self):
        pin = self.pin_entry.get()
        if pin.isdigit() and len(pin) == 4:
            account_number = self.generate_account_number()
            new_account = Account(account_number=account_number, pin=pin, balance=0)
            self.atm.add_account(new_account)
            messagebox.showinfo("Account Created", f"Your account number is: {account_number}")
            self.create_login_widgets()
        else:
            messagebox.showerror("Invalid PIN", "PIN must be a 4-digit number.")

    def create_login_widgets(self):
        self.clear_frame()

        tk.Label(self.main_frame, text="Account Login", font=('Helvetica', 16)).pack(pady=10)

        tk.Label(self.main_frame, text="Enter Account Number:").pack()
        self.account_number_entry = tk.Entry(self.main_frame)
        self.account_number_entry.pack()

        tk.Label(self.main_frame, text="Enter PIN:").pack()
        self.login_pin_entry = tk.Entry(self.main_frame, show='*')
        self.login_pin_entry.pack()

        tk.Button(self.main_frame, text="Login", command=self.login).pack(pady=5)
        tk.Button(self.main_frame, text="Back", command=self.create_account_widgets).pack(pady=5)

    def login(self):
        account_number = self.account_number_entry.get()
        pin = self.login_pin_entry.get()
        self.user_account = self.atm.authenticate(account_number, pin)
        if self.user_account:
            self.create_transaction_widgets()
        else:
            messagebox.showerror("Login Failed", "Invalid account number or PIN.")

    def create_transaction_widgets(self):
        self.clear_frame()

        tk.Label(self.main_frame, text="Transaction Menu", font=('Helvetica', 16)).pack(pady=10)

        tk.Button(self.main_frame, text="Check Balance", command=self.check_balance).pack(pady=5)
        tk.Button(self.main_frame, text="Deposit", command=self.create_deposit_widgets).pack(pady=5)
        tk.Button(self.main_frame, text="Withdraw", command=self.create_withdraw_widgets).pack(pady=5)
        tk.Button(self.main_frame, text="Transaction History", command=self.show_transaction_history).pack(pady=5)
        tk.Button(self.main_frame, text="Logout", command=self.create_login_widgets).pack(pady=5)
        
    def create_deposit_widgets(self):
        self.clear_frame()

        tk.Label(self.main_frame, text="Deposit Money", font=('Helvetica', 16)).pack(pady=10)

        tk.Label(self.main_frame, text="Enter amount to deposit:").pack()
        self.deposit_entry = tk.Entry(self.main_frame)
        self.deposit_entry.pack()

        tk.Button(self.main_frame, text="Deposit", command=self.deposit).pack(pady=5)
        tk.Button(self.main_frame, text="Back", command=self.create_transaction_widgets).pack(pady=5)

    def deposit(self):
        amount = self.deposit_entry.get()
        if amount.isdigit() and int(amount) > 0:
            self.user_account.deposit(int(amount))
            messagebox.showinfo("Deposit Successful", f"{amount} deposited successfully.")
            self.create_transaction_widgets()
        else:
            messagebox.showerror("Invalid Amount", "Please enter a valid amount.")

    def create_withdraw_widgets(self):
        self.clear_frame()

        tk.Label(self.main_frame, text="Withdraw Money", font=('Helvetica', 16)).pack(pady=10)

        tk.Label(self.main_frame, text="Enter amount to withdraw:").pack()
        self.withdraw_entry = tk.Entry(self.main_frame)
        self.withdraw_entry.pack()

        tk.Button(self.main_frame, text="Withdraw", command=self.withdraw).pack(pady=5)
        tk.Button(self.main_frame, text="Back", command=self.create_transaction_widgets).pack(pady=5)

    def withdraw(self):
        amount = self.withdraw_entry.get()

    
# ::contentReference[oaicite:0]{index=0}

 

# print("this line")
def generate_account_number():
    # Generate a random 10-digit number ensuring it doesn't start with zero
    return str(random.randint(10000, 99999))

def create_pin():
    while True:
        pin = input("Create a 4-digit PIN: ")
        if pin.isdigit() and len(pin) == 4:
            return pin
        else:
            print("Invalid PIN. Please enter exactly 4 digits.")

def main():
    atm = ATM()

    # Generate a new account number
    account_number = generate_account_number()
    print(f"Your new account number is: {account_number}")

    # Prompt user to create a PIN
    pin = create_pin()

    # Create a new account with the generated account number and user-defined PIN
    new_account = Account(account_number=account_number, pin=pin, balance=0)
    atm.add_account(new_account)

    print("Account created successfully!")

    # User authentication and transaction process
    print("\nWelcome to the ATM")
    entered_account_number = input("Enter your account number: ")
    entered_pin = input("Enter your PIN: ")

    user_account = atm.authenticate(entered_account_number, entered_pin)

    if user_account:
        while True:
            print("\nOptions:")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Transaction History")
            print("5. Exit")
            choice = input("Select an option: ")

            if choice == "1":
                print(f"Current Balance: {user_account.get_balance()}")
            elif choice == "2":
                amount = float(input("Enter deposit amount: "))
                if user_account.deposit(amount):
                    print(f"{amount} deposited successfully.")
                else:
                    print("Invalid deposit amount.")
            elif choice == "3":
                amount = float(input("Enter withdrawal amount: "))
                if user_account.withdraw(amount):
                    print(f"{amount} withdrawn successfully.")
                else:
                    print("Invalid withdrawal amount or insufficient funds.")
            elif choice == "4":
                print("Transaction History:")
                for transaction in user_account.get_transaction_history():
                    print(transaction)
            elif choice == "5":
                print("Thank you for using the ATM. Have a GoodDay!!")
                break
            else:
                print("Invalid option. Please try again.")
    else:
        print("Authentication failed. Please check your account number and PIN.")

if __name__ == "__main__":
    main()
