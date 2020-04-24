#1. Overrinding and the super() method

class Employee:
    def setNumberOfworkingHOurs(self):
        self.numberOfWorkingHours = 40
    
    def displayNumberOfWorkingHours(self):
        print(self.numberOfWorkingHours)
    
class Trainee(Employee):
    def setNumberOfworkingHOurs(self):
        self.numberOfWorkingHours = 45
    
    def resetNumberOfWorkingHours(self):
        super().setNumberOfworkingHOurs()

employee = Employee()
employee.setNumberOfworkingHOurs()
print("Number of working hours of employee: ", end = ' ')
employee.displayNumberOfWorkingHours()
trainee = Trainee()
trainee.setNumberOfworkingHOurs()
print("Number of working hours of trainee: ", end = ' ')
trainee.displayNumberOfWorkingHours()
trainee.resetNumberOfWorkingHours()
print("Number of working hours of trainee after reset ", end = ' ')
trainee.displayNumberOfWorkingHours()


#2. The Diamond Shape Problem in Multiple Inheritance

class A:
    def method(self):
        print("This method belongs to class A")
    pass

class B(A):
    def method(self):
        print("This method belongs to class B")
    pass

class C(A):
    def method(self):
        print("This method belongs to class C")
    pass

class D(C,B):  # (X,Y) <- this order also matters
    pass

d = D()
d.method()

#3. Overloading an Operator

class Square:
    def __init__(self, side):
        self.side = side
        
    def __add__(squareOne, squareTwo):
        return((4 * squareOne.side) + (4 * squareTwo.side))
        
squareOne = Square(5) # 5 * 4 = 20
squareTwo = Square(10) # 10 * 4 = 40
print("Sum of sides of both the squares = ", squareOne + squareTwo)

#3. Overloading an Operator

class Square:
    def __init__(self, side):
        self.side = side
        
    def __add__(squareOne, squareTwo):
        return((4 * squareOne.side) + (4 * squareTwo.side))
        
squareOne = Square(5) # 5 * 4 = 20
squareTwo = Square(10) # 10 * 4 = 40
print("Sum of sides of both the squares = ", squareOne + squareTwo)


#3. Implementing an Abstract Base Class(ABC) 
from abc import ABCMeta, abstractmethod

class Shape(metaclass = ABCMeta):
    @abstractmethod
    def area(self):
        return 0

class Square(Shape):
    side = 4
    def area(self):
        print("Area of square: ", self.side * self.side)

class Rectangle(Shape):
    width = 5
    length = 10
    def area(self):
        print("Area of rectangle: ", self.width * self.length)
    
square = Square()
rectangle = Rectangle()
square.area()
rectangle.area()
#  We can't instantiate abstract class Shape
#  shape = Shape()  - will throw an error


#4. EXERCISE - POLYMORPHISM
'''
Create a class called Square and perform the following tasks -
(i) Create two objects for this class squareOne and squareTwo
(ii) Find the result of side of squareOne to the power of side of squareTwo
Example: If squareOne has length of 2cm each side and
squareTwo has a length of 4cm each side, squareOne ** squareTwo 
should return 16, which is 2 to the power of 4.
Hint: While performing SquareOne ** SquareTwo, you need to 
overload __pow__() method.
'''

class Square:
    def __init__(self, side):
        self.side = side

    # Overload the exponential operator
    def __pow__(squareOne, squareTwo):
        # Return side of squareOne to the power of side of squareTwo
        return squareOne.side ** squareTwo.side

squareOne = Square(2)
squareTwo = Square(4)
print("squareOne to the power of squareTwo = ", squareOne ** squareTwo)

