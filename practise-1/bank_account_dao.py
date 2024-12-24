from bank_account_data import BankAccountData

class BankAccountDAO:
    def __init__(self):
        # In-memory storage for demonstration purposes
        self._accounts = {}

    def create_account(self, account_number, account_name, initial_balance):
        if account_number in self._accounts:
            raise ValueError("Account with this number already exists.")
        
        account = BankAccountData(account_number, account_name, initial_balance)
        self._accounts[account_number] = account
        return account

    def get_account(self, account_number):
        account = self._accounts.get(account_number)
        if not account:
            raise ValueError("Account not found.")
        return account

    def update_account(self, account_number, account_name=None, balance=None):
        account = self.get_account(account_number)
        if account_name is not None:
            account.account_name = account_name
        if balance is not None:
            account.balance = balance
        return account

    def delete_account(self, account_number):
        if account_number in self._accounts:
            del self._accounts[account_number]
        else:
            raise ValueError("Account not found.")

    def list_accounts(self):
        return list(self._accounts.values())