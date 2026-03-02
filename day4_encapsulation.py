
#from ABC Module

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadtharea(self)
        print('area = length * breadth')
r = Rectangle()
r.area()
