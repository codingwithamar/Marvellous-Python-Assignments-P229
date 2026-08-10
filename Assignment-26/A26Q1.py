# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A26Q1.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-26\A26Q1.py
# Subject/Question : Write a Python program to implement a class named Demo with the following specifications:
# Description : 
# • The class should contain two instance variables: no1 and no2.
# • The class should contain one class variable named Value.
# • Define a constructor (__init__) that accepts two parameters and initializes the instance variables.
# • Implement two instance methods:
#       ◦ Fun() – displays the values of instance variables no1 and no2.
#       ◦ Gun() – displays the values of instance variables no1 and no2.
# 
# Create two objects of the Demo class as follows:
#       Obj1 = Demo(11, 21)
#       Obj2 = Demo(51, 101)
# 
# Call the instance methods in the given sequence:
#   Obj1.Fun()
#   Obj2.Fun()
#   Obj1.Gun()
#   Obj2.Gun()
# =============================================================================

class Demo :
    Value = 0       #Class Variable

    def __init__(self,No1,No2):     #Constructor
        print("Inside Constructor")
        self.No1 = No1              #Instance Vatibale
        self.No2 = No2              #Instance Varibale

    def Fun(self):                      #Instance Method
        print("Inside Fun() Instant Method")
        print("NO1 : ",self.No1)
        print("NO2 : ",self.No2)

    def Gun(self):                      #Instance Method
        print("Inside Gun() Instant Method")
        print("NO1 : ",self.No1)
        print("NO2 : ",self.No2)

def main():
    print("Class Demonstartion")

    #Create Object
    Obj1 = Demo(11, 21)
    Obj2 = Demo(51, 101)

    # Instance Methods with call
    Obj1.Fun()
    Obj2.Fun()
    Obj1.Gun()
    Obj2.Gun()

if __name__ == "__main__":
    main()