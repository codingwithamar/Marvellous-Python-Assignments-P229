# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A13Q1.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-13\A13Q1.py
# Subject : 1. Write a program which accepts length and width of rectangle and prints area.
# Description : Input : Length and Width pf rectangle Output Area of rectangle
# =============================================================================

def Rectangle(Value1, Value2):
    Result = Value1 * Value2
    #Formula : Area = length × width
    return Result

def main():
    print("Enter the Length : ")
    len = float(input())

    print("Enter the Width : ")
    wid = float(input())

    area = Rectangle(len, wid)

    print("Area of Reactangle is : ", area)


if __name__ == "__main__":
    main()
