# Parent class
class Bank:
    def __init__(self):
        self.__balance = 0   # Private balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


# Child class
class Customer(Bank):
    def deposit_money(self, amount):
        self.deposit(amount)


# Create object
customer = Customer()

# Deposit money
customer.deposit_money(5000)
customer.deposit_money(2000)

# Show final balance
print("Final Balance:", customer.get_balance())