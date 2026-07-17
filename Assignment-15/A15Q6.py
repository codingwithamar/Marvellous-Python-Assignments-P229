# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A15Q6.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-15\A15Q6.py
# Subject : 6. Write a lambda function using reduce() which accepts a list of numbers and returns the minimum element.
# Description : Min Value return
# =============================================================================



from functools import reduce

def ChotaDon(iNo1,iNo2):
    if iNo1 > iNo2:
        return iNo2    
    else:
        return iNo1

def main():
    print("Enter the list of Numbers : ")
    NumList = list(map(int,input().split()))
    
    Result = reduce(ChotaDon, NumList)
    print("Your Small Number is : ", Result)

if __name__ == "__main__":
    main()
    