# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A19Q1.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-19\A19Q1.py
# Subject : 1.Write a program which contains one lambda function which accepts 
# one parameter and return power of two.
# Description : Input : 4   Output : 16   -    Input : 6     Output : 64
# =============================================================================

Power = lambda iValue : 2 ** iValue 

def main():
    Value = int(input("Enter the Number : "))
    
    Result = Power(Value)

    print(Result)

if __name__ == "__main__":
    main()
    