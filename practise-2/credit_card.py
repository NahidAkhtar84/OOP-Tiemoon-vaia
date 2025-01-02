from typing import Any
from datetime import datetime, timedelta


class CreditCard:
    def __init__(self):
        self.__balance = 500000
        self.__daily_limit = 100000
        self.__maximum_per_transaction_limit = 20000
        self.__last_reset_date = datetime.now().date()

    def get_balance(self) -> float:
        return self.__balance

    def __deduct_balance(self, amount: float) -> None:
        self.__balance -= amount

    def __check_and_reset_daily_limit(self) -> None:
        current_date = datetime.now().date()
        if current_date > self.__last_reset_date:
            self.reset_daily_limit()
            self.__last_reset_date = current_date

    def withdraw(self, amount: float) -> Any:
        self.__check_and_reset_daily_limit()

        if self.__balance - amount < 0:
            raise Exception("Insufficient balance.")
        
        if self.__daily_limit - amount < 0:
            raise Exception("Daily limit exceeded.")
        
        if amount > self.__maximum_per_transaction_limit:
            raise Exception(f"Maximum per transaction limit is: {self.__maximum_per_transaction_limit}")
        
        self.__deduct_balance(amount)
        self.__daily_limit -= amount
        print(f"Withdrawal successful: {amount}")
        print(f"Remaining balance: {self.__balance}")
        print(f"Remaining daily limit: {self.__daily_limit}")

    def pay_bill(self, amount: float) -> Any:
        if self.__balance - amount < 0:
            raise Exception("Insufficient balance.")
        
        self.__deduct_balance(amount)
        print(f"Bill payment successful: {amount}")
        print(f"Remaining balance: {self.__balance}")

    def reset_daily_limit(self):
        self.__daily_limit = 100000
        print("Daily limit reset.")