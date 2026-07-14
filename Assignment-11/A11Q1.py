# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A11Q1.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-11\A11Q1.py
# Subject : 1. Write a program which accepts one number and checks whether it is prime or not.
# Description : Input: 11  Output: Prime Number
# =============================================================================

def CheckPrime(Number):
    if (Number % 2 != 0):
        print("This value is Prime : ", Number)
    else:
        print("This is not Prime Value")

def main():
    Value = int(input("Enter the number :"))
    CheckPrime(Value)

if __name__ == "__main__":
    main()
    