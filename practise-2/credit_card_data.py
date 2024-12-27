from dataclasses import dataclass

@dataclass
class CreditCardData:
    card_number: str
    balance: float
    maximum_limit: float
    monthly_spent: float
    daily_spent: float
    
