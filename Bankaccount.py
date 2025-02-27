class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited: {amount}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        else:
            self.balance -= amount
            return f"Withdrawn: {amount}"

    def check_balance(self):
        return f"Current Balance: {self.balance}"

    def customer_details(self):
        return f"Customer: {self.customer_name}, Account: {self.account_number}, Opened: {self.date_of_opening}, Balance: {self.balance}"


account = BankAccount("436 323", 5000, "2025/02/27", "Telvin")
print(account.deposit(2000))
print(account.withdraw(1000))
print(account.withdraw(7000))
print(account.check_balance())
print(account.customer_details())
