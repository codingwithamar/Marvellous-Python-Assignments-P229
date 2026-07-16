# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A14Q8.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-14\A14Q8.py
# Subject : 8. Write a lambda function which accepts two numbers and returns addition.
# Description : Addition
# =============================================================================

Addition = lambda liValue1, liValue2 : liValue1 + liValue2

def main():
    iValue1 = int(input("Enter the Value 1 : "))
    iValue2 = int(input("Enter the Value 2 : "))
    Ret = Addition(iValue1, iValue2)
    print("Addition is : ",Ret)

if __name__ == "__main__":
    main()
