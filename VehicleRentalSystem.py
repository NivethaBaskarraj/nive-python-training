from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self, vehicle, days):
        self.vehicle = vehicle
        self.days = days
        
    @abstractmethod
    def calculate_rent(self):
        pass

class Car(Vehicle):
    def __init__(self, vehicle, days):
        super().__init__(vehicle, days)
        self.rent_per_day = 1000

    def calculate_rent(self):
        rent = self.rent_per_day * self.days
        return rent
    
class Bike(Vehicle):
    def __init__(self, vehicle, days):
        super().__init__(vehicle, days)
        self.rent_per_day = 500

    def calculate_rent(self):
        rent = self.rent_per_day * self.days
        return rent
    
vehicle = input("Enter the vehicle type (Car/Bike): ")
days = int(input("Enter the number of days: "))
if vehicle.lower() == 'car':
    rental = Car(vehicle, days)
    print('Total Rent: ', rental.calculate_rent())
elif vechicle.lower() == 'bike':
    rental  = Bike(vehicle, days)
    print('Total Rent: ', rental.calculate_rent())
else:
    print("Invalid vehicle type.")