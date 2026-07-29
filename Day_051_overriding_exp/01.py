'''
Assignment 1: Shape Area Calculation

Create a parent class Shape with a method calculateArea() that prints "Area calculation not defined for Shape."

Create subclasses:

Circle that overrides calculateArea() to calculate and print the area of a circle.

Rectangle that overrides calculateArea() to calculate and print the area of a rectangle.

Write a Main class to demonstrate polymorphism using an array of Shape objects.
'''


class Shape:
   def calculateArea(self):
        print("Area calculation not defined for Shape.")

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def calculateArea(self): 
        area = 3.14 * self.r * self.r
        print(area)       
  
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculateArea(self): 
        area = self.length * self.width
        print(area)

#correct

class Main:

    def start(self):
        r = int(input("Enter r: "))
        length = int(input("length: "))
        width  = int(input("width: "))

        shapes = [Shape(), Circle(r), Rectangle(length, width)]

        for i in shapes:   
            i.calculateArea()

run = Main()
run.start()



'''
r = int(input("Enter r: "))
circle  = Circle(r)
circle.calculateArea()

length = int(input("length: "))
width  = int(input("width: "))
rectangle = Rectangle(length, width)
rectangle.calculateArea()
'''

 
