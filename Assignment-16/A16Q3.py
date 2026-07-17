# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A16Q3.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-16\A16Q3.py
# Subject : Write a program which contains one function named as Add() which accepts two 
# numbers from user and return addition of that two numbers.
# Description : Input : 11 5    Output : 16
# =============================================================================

def Add(iNum1,iNum2):
    return iNum1 + iNum2

def main():
    print("Enter the Number 1 :")
    Num1 = int(input())
    print("Enter the Number 1 :")
    Num2 = int(input())

    Ret = Add(Num1,Num2)
    print(Ret)


if __name__ == "__main__":
    main()
