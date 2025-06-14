class BankAccount:

    def __init__(self, initial_balance=0):
        self.__account_balance = float(initial_balance)

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Successfully deposited ${amount:.2f}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):

        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if self.__account_balance >= amount:
            self.__account_balance -= amount
            print(f"Successfully withdrew ${amount:.2f}.")
            return True
        else:

            return False

    def display_balance(self):

        print(f"Current Balance: ${self.__account_balance:.2f}")
