from abc import ABC, abstractmethod
class Shape(ABC):
    def __init__(self, shape_type):
        self.shape_type = shape_type
        
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, shape_type, radius):
        super().__init__(shape_type)
        self.radius = radius

    def area(self):
        area_of_circle = 3.14 * self.radius * self.radius
        return area_of_circle
    
class Rectangle(Shape):
    def __init__(self, shape_type, length, breadth):
        super().__init__(shape_type)
        self.length = length
        self.width = breadth

    def area(self):
        area_of_rectangle = self.length * self.width
        return area_of_rectangle
    
shape_type = input("Enter the shape type (Circle/Rectangle): ")
if shape_type.lower() == 'circle':
    radius = float(input("Enter the radius of the circle: "))
    shape1 = Circle(shape_type, radius)
    print('Area of Circle: ', shape1.area())
elif shape_type.lower() == 'rectangle':
    length = float(input("Enter the length of the rectangle: "))
    breadth = float(input("Enter the breadth of the rectangle: "))
    shape2 = Rectangle(shape_type, length, breadth)
    print('Area of Rectangle: ', shape2.area())
else:
    print("Invalid shape type.")