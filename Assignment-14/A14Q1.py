# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A14Q1.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-14\A14Q1.py
# Subject : 1. Write a lambda function which accepts one number and returns square of that number.
# Description : Formula : Square = Number × Number
# =============================================================================

Square = lambda liValue : liValue * liValue

def main():
    iValue = int(input("Enter the Value : "))
    Ret = Square(iValue)
    print("Square Of area is : ",Ret)


if __name__ == "__main__":
    main() 
    