# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A16Q7.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-16\A16Q7.py
# Subject : 7. Write a program which contains one function that accept one number from user and 
# returns true if number is divisible by 5 otherwise return false.
# Description : Input : 8 Output : False    Input : 25 Output : True
# =============================================================================

def bool(iNo):
    if iNo%5 == 0:
        return True
    else:
        return False

def main():
    print("Enter the Numbetr")
    No = int(input())
    Ret = bool(No)
    print(Ret)

if __name__ == "__main__":
    main()
    
