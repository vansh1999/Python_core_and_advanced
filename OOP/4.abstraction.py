# Abstraction - Abstraction is used to hide the internal details and show only functionalities.
# data abstraction is achieved through encapsulation.



# Creating Abstract Classes

# lets say we have two class Shape and Square, 
'''
class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass

class square(Shape):
    def __init__(self,side):
        self.__side = side

s = Shape()  # right now we are able to create instance of Shape class
'''
# we want two things --
#1. we dont want user to create instance object of class Shape, because it acts like template for square class
#2. both the Shape methods are implemented in square class

# How to achieve that, we make use of abstract class 
# how to make abstract class

from abc import ABC , abstractmethod

class Shape(ABC):   # abstract class , abc

    @abstractmethod  # abstract method
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Square(Shape):

    def __init__(self , side):
        self.__side = side

    def area(self):
        return self.__side * self.__side

    def perimeter(self):
        return 4 * self.__side


s = Square(3)
print(s.area())
print(s.perimeter())



# Interface 
# abstract class in which all methods are abstract methods , then it is called Interface

# If all methods inside abstract class are abstract method , then it is called Interface

