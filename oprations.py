def main():
    atm = ATM()

    # Adding a sample account
    sample_account = Account(account_number="123456789", pin="1234", balance=1000)
    atm.add_account(sample_account)

    print("Welcome to the ATM")
    account_number = input("Enter your account number: ")
    pin = input("Enter your PIN: ")

    user_account = atm.authenticate(account_number, pin)

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
                print(f"Current Balance: ${user_account.get_balance()}")
            elif choice == "2":
                amount = float(input("Enter deposit amount: "))
                if user_account.deposit(amount):
                    print(f"${amount} deposited successfully.")
                else:
                    print("Invalid deposit amount.")
            elif choice == "3":
                amount = float(input("Enter withdrawal amount: "))
                if user_account.withdraw(amount):
                    print(f"${amount} withdrawn successfully.")
                else:
                    print("Invalid withdrawal amount or insufficient funds.")
            elif choice == "4":
                print("Transaction History:")
                for transaction in user_account.get_transaction_history():
                    print(transaction)
            elif choice == "5":
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")
    else:
        print("Authentication failed. Please check your account number and PIN.")

if __name__ == "__main__":
    main()
