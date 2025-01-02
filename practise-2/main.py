from credit_card import CreditCard


def main():
    card = CreditCard()

    print("Initial balance:", card.get_balance())

    try:
        card.withdraw(15000)
        card.withdraw(5000)

        # Simulate end of the day
        print("\nSimulating next day...")
        card.reset_daily_limit()
        card.withdraw(20000)
    except Exception as e:
        print("Error:", e)

    try:
        print("\nPaying a bill...")
        card.pay_bill(50000)
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()