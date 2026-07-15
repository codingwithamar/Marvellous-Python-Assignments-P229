# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A13Q2.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-13\A13Q2.py
# Subject : 2. Write a program which accepts radius of circle and prints area of circle.
# Description : Input : value of Radius     Output : Area of Circle
# =============================================================================

def Circle(ValueOfRadius):
    pi = 3.14
    R = ValueOfRadius

    #Formula : Area Of Circle = Pi * (Radius*Radius)
    Result = pi * R**2
    return Result


def main():
    Radius =float(input("Enter the value Of Radius : "))
    AreaOfCircle = Circle(Radius)
    print("Area of Circle is : ", AreaOfCircle)

if __name__ == "__main__":
    main()
    