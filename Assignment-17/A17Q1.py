# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A17Q1.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-17\A17Q1.py
# Subject : 1.Create on module named as Arithmetic which contains 4 functions as Add() for addition, 
# Sub() for subtraction, Mult() for multiplication and Div() for division. All functions accepts 
# two parameters as number and perform the operation. Write on python program which call all 
# the functions from Arithmetic module by accepting the parameters from user.
# Description : Create Arithmatic Module and use in main()
# =============================================================================

import Arithmatic

def main():
    print("Enter Value1")
    Value1 = int(input())
    print("Enter Value2")
    Value2 = int(input())

    Addition = Arithmatic.Add(Value1,Value2)
    print("Addition is :",Addition)

    Substraction = Arithmatic.Sub(Value1,Value2)
    print("Substraction is :",Substraction)

    Multiplication = Arithmatic.Mult(Value1,Value2)
    print("Multiplication is :",Multiplication)

    Division = Arithmatic.Div(Value1,Value2)
    print("Division is : ",Division)

if __name__ == "__main__":
    main()
    