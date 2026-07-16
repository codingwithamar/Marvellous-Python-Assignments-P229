# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A14Q9.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-14\A14Q9.py
# Subject : 9. Write a lambda function which accepts two numbers and returns multiplication.
# Description : Multiplication
# =============================================================================

Multiplication = lambda liValue1, liValue2 : liValue1 * liValue2

def main():
    iValue1 = int(input("Enter the Value 1 : "))
    iValue2 = int(input("Enter the Value 2 : "))
    Ret = Multiplication(iValue1, iValue2)
    print("Multiplication is : ",Ret)

if __name__ == "__main__":
        main()
        