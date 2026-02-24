#create a class to perform various functions
class Grade:
    def __init__(self):
        self.marks = []
        self.result = []
        self.total = 0
        self.number = 0
        
    #function to obtain number of students from the user == N students
    def get_marks(self):
        self.number = int( input( 'Enter how many students:'))
        for i in range(self.number):
            mark = int(input( 'Enter the marks:'))
            self.marks.append(mark)
        return self.marks

    #function to calculate the mark and add them in a list
    def calculate_mark(self):
        self.result = []
        for i in self.marks:
            if i < 0 or i > 100:
                self.result.append('Invalid Marks')
            elif i >= 40:
                self.result.append('Pass')
            else:
                self.result.append('Fail')
        else:
            self.result.append('Invalid Marks')
        return self.result

    #function to calculate the total marks
    def total_marks(self):
        self.total = 0
        for i  in self.marks:
            self.total = self.total + i
        print('Total marks is: ', self.total)
        return self.total
    
    #function to calculate the average marks
    def average_marks(self):
        if self.number > 0:
            self.average = self.total / self.number
        else:
            self.average = 0
        print('The average marks is: ', self.average) 
        return self.average
    
    #function to count the number of students who passed
    def number_of_passed_stu(self):
        return self.result.count('Pass')
    
    #function to count the number of students who failed
    def number_of_failed_stu(self):
        return self.result.count('Fail')

#creation of object to access the class methods    
obj_grade = Grade ()
obj_grade.get_marks()
obj_grade.calculate_mark()
obj_grade.total_marks()
obj_grade.average_marks()
print('Passed student count: ', obj_grade.number_of_passed_stu())
print('Failed student count: ', obj_grade.number_of_failed_stu())