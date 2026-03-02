from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self, emp_type):
        self.emp_type = emp_type
        self.salary = 0

    @abstractmethod
    def employee_type(self):
        pass

class Permanent_employee(Employee):
    def __init__(self, emp_type):
        super().__init__(emp_type)
        self.salary = 50000

    def employee_type(self):
        return self.emp_type
    
    def calculate_salary(self):
        return self.salary
    
class Contract_employee(Employee): 
    def __init__(self, emp_type, working_hours):
        super().__init__(emp_type)
        self.working_hours = working_hours
        self.salary_per_hour = 500

    def employee_type(self):
        return self.emp_type

    def calculate_salary(self):
        self.salary = self.working_hours * self.salary_per_hour
        return self.salary

emp_type = input("Enter the employee type (Permanent/Contract): ")
if emp_type.lower() == 'permanent':
    emp1 = Permanent_employee(emp_type)
    print('Salary: ', emp1.calculate_salary())
elif emp_type.lower() == 'contract':
    working_hours = int(input("Enter the working hours: "))
    emp1 = Contract_employee(emp_type, working_hours)
    print('Salary: ', emp1.calculate_salary())
else:
    print("Invalid employee type.")