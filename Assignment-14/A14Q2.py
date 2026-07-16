# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A14Q2.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-14\A14Q2.py
# Subject : 2. Write a lambda function which accepts one number and returns cube of that number.
# Description : Formula : Cube = Number * Number * Number
# =============================================================================

Cube = lambda liValue : liValue**3

def main():
    iValue = int(input("Enter the Value : "))
    Ret = Cube(iValue)
    print("Cube Of area is : ",Ret)

if __name__ == "__main__":
    main() 
    