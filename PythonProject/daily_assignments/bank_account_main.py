class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = balance

    def get_account_holder(self):
        return self.__account_number

    def get_account_holder(self):
        return self.__account_holder

    def get_balance(self):
        return self.__balance

    def set_account_holder(self, name):
        self.__account_holder = name

    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance")
        elif amount <= 0:
            print("Invalid withdrawl amount")
        else:
            self.__balance -= amount
            print("Withdrawn:", amount)

    def display(self):
        print("\nAccount Details:")
        print("Account Number:", self.__account_number)
        print("Balance:", self.__balance)

account1 = BankAccount(101, "Sanjay", 1000)

account1.display()

account1.deposit(500)
account1.withdraw(300)
account1.withdraw(1500)

account1.display()


