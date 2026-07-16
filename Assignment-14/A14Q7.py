# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A14Q7.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-14\A14Q7.py
# Subject : 7. Write a lambda function which accepts one number and returns True if divisible by 5.
# Description : Divisible by 5 True and False
# =============================================================================

Divisibility = lambda liValue : True if liValue%5==0 else False

def main():
    iValue = int(input("Enter the Value : "))
    Ret = Divisibility(iValue)
    if Ret == True:
        print("Value is True mean Value is Divisible by 5")
    else:
        print("Value is False Mean Not Divisible by 5")
        


if __name__ == "__main__":
    main()
