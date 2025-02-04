from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):
    @abstractmethod
    def area(self):
        return  0

class Square(Shape):
    side = 4
    def area(self):
        print("Area: ", self.side*self.side)

class Rtangle(Shape):
    width = 5
    length = 10
    def area(self):
        print("Area: ", self.width*self.length)

        # // *[ @ id = "question"] / div[2] / div[2] / div[1] / p[2]

square = Square()
rectangle = Rtangle()
square.area()
rectangle.area()

shape = Shape() # throws error as it not lets instantiate objects for abstract class
# abstract class can only be inherited in derived classes
# a base class which consists of abstract methods that should
# be implemented in its derived class is an abstract class