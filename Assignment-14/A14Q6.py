# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A14Q6.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-14\A14Q6.py
# Subject : 6. Write a lambda function which accepts one number and returns True if number is odd otherwise False.
# Description : Find odd
# =============================================================================


EvenOdd = lambda liValue : True if liValue % 2 != 0 else False

def main():
    iValue = int(input("Enter the Value : "))
    Ret = EvenOdd(iValue)
    if Ret == True:
        print("Value is True mean Odd")
    else:
        print("Value is False mean Even")
        
if __name__ == "__main__":
    main()
    