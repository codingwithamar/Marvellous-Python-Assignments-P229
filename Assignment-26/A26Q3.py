# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A26Q3.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-26\A26Q3.py
# Subject/Question : Write a Python program to implement a class named Arithmetic 
# with the following characteristics:
# Description : 
# • The class should contain two instance variables: Value1 and Value2.
# • Define a constructor (__init__) that initializes all instance variables to 0.
# • Implement the following instance methods:
#       ◦ Accept() – accepts values for Value1 and Value2 from the user.
#       ◦ Addition() – returns the addition of Value1 and Value2.
#       ◦ Subtraction() – returns the subtraction of Value1 and Value2.
#       ◦ Multiplication() – returns the multiplication of Value1 and Value2.
#       ◦ Division() – returns the division of Value1 and Value2 
#                       (handle division by zeroproperly).
# • Create multiple objects of the Arithmetic class and invoke all the instance methods.
# =============================================================================

class Arithmatic:
    def __init__(self,Value1, Value2):
        print("Inside Constructor")
        self.Value1 = Value1
        self.Value2 = Value2
        print()

    def Accept(self):
        print("Inside Accept")
        self.Value1 = int(input("Enter the Value1 Values :"))
        self.Value2 = int(input("Enter the Value2 Values :"))  
        print("Value1 is : ",self.Value1)      
        print("Value2 is : ",self.Value2)     
        print()

    def Addition(self):
        print("Inside Addition")
        AddResult = self.Value1 + self.Value2
        print("Addition is : ",AddResult)
        print()

    def Substraction(self):
        print("Inside Substraction")
        SubResult = self.Value1 - self.Value2
        print("Substraction is : ",SubResult)
        print()

    def Multiplication(self):
        print("Inside Multiplication")
        MultResult = self.Value1 * self.Value2
        print("Multiplication is : ",MultResult)
        print()

    def Division(self):
        print("Inside Division")
        DivResult = self.Value1 / self.Value2
        print("Division is : ",DivResult)
        print()


def main():
    Value1 = 0
    Value2 = 0
    Obj1 = Arithmatic(Value1,Value2)
    Obj1.Accept()
    Obj1.Addition()
    Obj1.Substraction()
    Obj1.Multiplication()
    Obj1.Division()

    Obj2 = Arithmatic(Value1,Value2)
    Obj2.Accept()
    Obj2.Addition()
    Obj2.Substraction()
    Obj2.Multiplication()
    Obj2.Division()

if __name__ == "__main__":
    main()
    