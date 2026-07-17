# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A15Q4.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-15\A15Q4.py
# Subject : 4. Write a lambda function using reduce() which accepts a list of numbers and returns the addition of all elements.
# Description : Input : 1 2 3 4 5   OUTPUT : 15
# =============================================================================

from functools import reduce

def Addition(iNo1,iNo2):
    return iNo1 + iNo2

def main():
    print("Enter the list of Numbers : ")
    NumList = list(map(int,input().split()))
    
    Result = reduce(Addition, NumList)
    print("Your All Numbers Addition is : ", Result)

if __name__ == "__main__":
    main()
