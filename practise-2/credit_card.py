from typing import Any
from datetime import datetime


class CreditCard:
    def __init__(self):
        self.__balance = 500000
        self.__daily_limit = 100000
        self.__maximum_per_transaction_limit = 20000
        self.__today = datetime.date()


    def get_balance(self) -> float:
        return self.__balance


    def __deduct_balance(self, amount: float) -> None:
        self.balance -= amount

    def withdraw(self, amount: float, current_date) -> Any:
        if self.__balance - amount < 0:
            raise Exception("Insufficient balance.")
        
        if self.__daily_limit - amount < 0:
            raise Exception("Daily limit exceeded.")
        
        if amount > self.__maximum_per_transaction_limit:
            raise Exception(f"Maximum per transaction limit is: {self.__maximum_per_transaction_limit}")
        
        self.__deduct_balance(amount)
        self.__daily_limit -= amount


    def pay_bill(self, amount: float) -> Any:
        if self.__balance - amount < 0:
            raise Exception("Insufficient balance.")
        
        self.__deduct_balance(amount)
        

    def reset_daily_limit(self):
        self.__daily_limit = 100000