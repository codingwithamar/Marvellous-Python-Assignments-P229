# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A26Q2.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-26\A26Q2.py
# Subject/Question : 
# Write a Python program to implement a class named Circle with the following requirements:
# Description : 
# • The class should contain three instance variables: Radius, Area, and Circumference.
# • The class should contain one class variable named PI, initialized to 3.14.
# • Define a constructor (__init__) that initializes all instance variables to 0.0.
# • Implement the following instance methods:
#       ◦ Accept() – accepts the radius of the circle from the user.
#       ◦ CalculateArea() – calculates the area of the circle and stores it in the Area variable.
#       ◦ CalculateCircumference() – calculates the circumference of the circle and stores it in the Circumference variable.
#       ◦ Display() – displays the values of Radius, Area, and Circumference.
# • Create multiple objects of the Circle class and invoke all the instance methods for each object.
# =============================================================================

class Circle:
    PI = 3.14

    def __init__(self):
        print("Inside Constructor")
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0
        print()

    def Accept(self):
        print("Inside Radius")
        self.Radius = int(input("Enter the Radius of Circle : "))
        print("Your Entered Radius is : ",self.Radius)
        print()

    def CalculateArea(self):
        print("Inside Area")
        self.Area = self.PI * (self.Radius**2)
        print("Area of Circle is : ",self.Area)
        print()

    def CalculateCircumference(self):
        print("Inside Circumference")
        self.Circumference = 2 * self.PI * self.Radius
        print("Circumference Of Circle is : ",self.Circumference)
        print()

    def Display(self):
        print("Inside Display")
        print("Display.Radius : ",self.Radius)
        print("Display.Area : ",self.Area)
        print("Display.Circumference : ",self.Circumference)
        print()

def main():
    Obj1 = Circle()
    Obj1.Accept()
    Obj1.CalculateArea()
    Obj1.CalculateCircumference()
    Obj1.Display()

    Obj2 = Circle()
    Obj2.Accept()
    Obj2.CalculateArea()
    Obj2.CalculateCircumference()
    Obj2.Display()

    Obj3 = Circle()
    Obj3.Accept()
    Obj3.CalculateArea()
    Obj3.CalculateCircumference()
    Obj3.Display()    

if __name__ == "__main__":
    main()