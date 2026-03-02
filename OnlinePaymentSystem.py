from  abc import ABC, abstractmethod
class Payment(ABC):
    def __init__(self, amount):
        self.amount = amount

    @abstractmethod
    def pay(self):
        pass

class UPI(Payment):
    def __init__(self, amount):
        super().__init__(amount)

    def pay(self):
        print(f"Paid $ {self.amount} using UPI")
        return self.amount
    
class Card(Payment):
    def __init__(self, amount):
        super().__init__(amount)

    def pay(self):
        print(f"Paid $ {self.amount} using Card")
        return self.amount
    
class Cash(Payment):
    def __init__(self, amount):
        super().__init__(amount)

    def pay(self):
        print(f"Paid $ {self.amount} using Cash")
        return self.amount
    
mode = input("Enter the payment mode (UPI/Card/Cash): ")
amount = int(input("Enter the amount: "))
if mode.lower() == 'upi':
    payment = UPI(amount)
    payment.pay()
elif mode.lower() == 'card':
    payment = Card(amount)
    payment.pay()
elif mode.lower() == 'cash':
    payment = Cash(amount)
    payment.pay()
else:
    print("Invalid payment mode.")