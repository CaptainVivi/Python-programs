class Account:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited Rs. {amount}. Current balance is Rs. {self.balance}")
        else:
            print("Deposit amount should be greater than zero.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrawn Rs. {amount}. Current balance is Rs. {self.balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount should be greater than zero.")

    def display_balance(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: Rs. {self.balance}")

class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, balance=0.0, min_balance=500.0):
        super().__init__(account_number, account_holder, balance)
        self.min_balance = min_balance

    def withdraw(self, amount):
        if self.balance - amount < self.min_balance:
            print("Withdrawal amount exceeds minimum balance limit.")
        else:
            super().withdraw(amount)

class CurrentAccount(Account):
    def __init__(self, account_number, account_holder, balance=0.0, overdraft_limit=10000.0):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            print("Withdrawal amount exceeds overdraft limit.")
        else:
            super().withdraw(amount)

def main():
    # Create Savings Account
    savings_acc = SavingsAccount("SAV-001", "Jenna Myers", 10000.0, 500.0)
    savings_acc.display_balance()
    savings_acc.deposit(500.0)
    savings_acc.withdraw(200.0)
    savings_acc.withdraw(900.0)

    # Create Current Account
    current_acc = CurrentAccount("CUR-001", "Jane Doe", 5000.0, 10000.0)
    current_acc.display_balance()
    current_acc.deposit(1000.0)
    current_acc.withdraw(7000.0)
    current_acc.withdraw(8000.0)

if __name__ == "__main__":
    main()
