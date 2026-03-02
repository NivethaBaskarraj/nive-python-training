from abc import ABC, abstractmethod
class BankAccount(ABC):
    def __init__(self, name, balance):
        self.time = 1
        self.interest_rate = 0.04
        self.name = name
        self.__balance = balance
    
    @abstractmethod
    def calculate_interest(self):
        pass

class SavingsAccount(BankAccount):
    def __init__(self, name, balance):
        super().__init__(name, balance)
        self.__balance = 0
        self.time = 1
        self.interest_rate = 0.04

    def get_input(self, name, balance):
        self.name = name
        self.__balance = balance

    def calculate_interest(self):
        interest = self.__balance * self.interest_rate * self.time
        return interest

class CheckingAccount(BankAccount):
    def __init__(self, name, balance):
        super().__init__(name, balance)
        self.name = name
        self.__balance  = balance

    def calculate_interest(self):
        self.interest = self.__balance * self.interest_rate * self.time
        return float(self.interest)
           
name = input("Enter the name: ")
balance = int(input("Enter the balance: "))
account1 = CheckingAccount(name, balance)
print('Balance: ', account1._BankAccount__balance)
print('Interest: ', account1.calculate_interest())