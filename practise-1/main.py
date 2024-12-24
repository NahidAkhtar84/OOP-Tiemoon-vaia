from bank_account_dao import BankAccountDAO
from bank_account import BankAccount


def main():
    # Create a BankAccountDAO instance
    dao = BankAccountDAO()

    print("Welcome to the Bank Account Management System!")
    print("Choose an option from the menu below:")

    while True:
        print("\nMenu:")
        print("1. Create Account")
        print("2. View Account Details")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Transfer")
        print("6. List All Accounts")
        print("7. Delete Account")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            account_number = input("Enter account number: ")
            account_name = input("Enter account name: ")
            initial_balance = float(input("Enter initial balance: "))
            try:
                dao.create_account(account_number, account_name, initial_balance)
                print("Account created successfully!")
            except ValueError as e:
                print(e)

        elif choice == "2":
            account_number = input("Enter account number: ")
            try:
                account = dao.get_account(account_number)
                print(f"Account Details:\nNumber: {account.account_number}, Name: {account.account_name}, Balance: {account.balance}")
            except ValueError as e:
                print(e)

        elif choice == "3":
            account_number = input("Enter account number: ")
            try:
                account = dao.get_account(account_number)
                amount = float(input("Enter amount to deposit: "))
                account.balance += amount
                print(f"Deposited successfully! New Balance: {account.balance}")
            except ValueError as e:
                print(e)

        elif choice == "4":
            account_number = input("Enter account number: ")
            try:
                account = dao.get_account(account_number)
                amount = float(input("Enter amount to withdraw: "))
                if amount > account.balance:
                    print("Insufficient balance!")
                else:
                    account.balance -= amount
                    print(f"Withdrawn successfully! New Balance: {account.balance}")
            except ValueError as e:
                print(e)

        elif choice == "5":
            from_account_number = input("Enter sender's account number: ")
            to_account_number = input("Enter receiver's account number: ")
            amount = float(input("Enter amount to transfer: "))
            try:
                from_account = dao.get_account(from_account_number)
                to_account = dao.get_account(to_account_number)
                if amount > from_account.balance:
                    print("Insufficient balance!")
                else:
                    from_account.balance -= amount
                    to_account.balance += amount
                    print(f"Transferred successfully! New Balance of {from_account.account_name}: {from_account.balance}, "
                          f"{to_account.account_name}: {to_account.balance}")
            except ValueError as e:
                print(e)

        elif choice == "6":
            accounts = dao.list_accounts()
            if not accounts:
                print("No accounts found.")
            else:
                print("Accounts:")
                for account in accounts:
                    print(f"Number: {account.account_number}, Name: {account.account_name}, Balance: {account.balance}")

        elif choice == "7":
            account_number = input("Enter account number to delete: ")
            try:
                dao.delete_account(account_number)
                print("Account deleted successfully!")
            except ValueError as e:
                print(e)

        elif choice == "8":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
