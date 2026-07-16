# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A14Q5.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-14\A14Q5.py
# Subject : 5. Write a lambda function which accepts one number and returns True if number is even otherwise False.
# Description : Even and Odd find
# =============================================================================

EvenOdd = lambda liValue : True if liValue%2==0 else False

def main():
    iValue = int(input("Enter the Value : "))
    Ret = EvenOdd(iValue)
    if Ret == True:
        print("Value is True mean Even")
    else:
        print("Value is False mean Odd")
        

if __name__ == "__main__":
    main()
    