# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A19Q2.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-19\A19Q2.py
# Subject : 2.Write a program which contains one lambda function which accepts
#  two parameters and return its multiplication.
# Description : Description
# =============================================================================

Multiplication = lambda iValue1,iValue2 : iValue1 * iValue2

def main():
    print("Enter the Number1")
    Value1 = int(input())
    
    print("Enter the Number2")
    Value2 = int(input())

    Result = Multiplication(Value1,Value2)
    print("Your Multiplication is : ", Result)

if __name__ == "__main__":
    main()
    