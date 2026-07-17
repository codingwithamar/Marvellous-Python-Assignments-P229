# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A15Q5.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-15\A15Q5.py
# Subject : 5. Write a lambda function using reduce() which accepts a list of numbers and returns the maximum element.
# Description : Max Value Return
# =============================================================================

from functools import reduce
def BigBull(iNo1,iNo2):
    if iNo1 > iNo2:
        return iNo1    
    else:
        return iNo2

def main():
    print("Enter the list of Numbers : ")
    NumList = list(map(int,input().split()))
    
    Result = reduce(BigBull, NumList)
    print("Your Big Number is : ", Result)

if __name__ == "__main__":
    main()
    