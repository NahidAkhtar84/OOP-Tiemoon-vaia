from dataclasses import dataclass

@dataclass
class BankAccountData:
    account_number: str
    account_name: str
    balance: float