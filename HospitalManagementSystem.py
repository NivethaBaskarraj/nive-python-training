from abc import ABC, abstractmethod
class Patient(ABC):
    def __init__(self, patient_type):
        self.patient_type = patient_type
        self.total_bill = 0

    @abstractmethod
    def calculate_bill(self):
        pass

class InPatient(Patient):
    def __init__(self, patient_type):
        super().__init__(patient_type)
        self.total_bill = 0

    def calculate_bill(self):
        self.total_bill = 20000
        return self.total_bill
    
class OutPatient(Patient):
    def __init__(self, patient_type):
        super().__init__(patient_type)
        self.total_bill = 0

    def calculate_bill(self):
        self.total_bill = 10000
        return self.total_bill
    
patient_type = input("Enter the patient type (InPatient/OutPatient): ")
if patient_type.lower() == 'inpatient':
    patient1 = InPatient(patient_type)
    print('Total Bill: ', patient1.calculate_bill())
elif patient_type.lower() == 'outpatient':
    patient1 = OutPatient(patient_type)
    print('Total Bill: ', patient1.calculate_bill())
else:
    print("Invalid patient type.")