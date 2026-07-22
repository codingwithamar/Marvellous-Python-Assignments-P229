# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A19Q5.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-19\A19Q5.py
# Subject : 5.Write a program which contains filter(), map() and reduce() in it. 
# Python application which contains one list of numbers. List contains the numbers 
# which are accepted from user. Filter should filter out all prime numbers. 
# Map function will multiply each number by 2. Reduce will return Maximum number from 
# that numbers. (You can also use normal functions instead of lambda functions).
# Description : 
#Input List = [2, 70 , 11, 10, 17, 23, 31, 77]
#List after filter = [2, 11, 17, 23, 31]
#List after map = [4, 22, 34, 46, 62]
#Output of reduce = 62
# =============================================================================

from functools import reduce

def PrimeNumbers(iValues):
    for i in range(2,iValues):
        if iValues%i==0:
            return False
        return True
    
Multiplication = lambda iValues : iValues * 2

def Max(iValue1,iValue2):
    if iValue1 < iValue2:
        return iValue2

def main():
    print("Enter the list of Numbers")
    Values = list(map(int,input().split()))
    
    fValues = list(filter(PrimeNumbers,Values))
    print("List after Filter : ", fValues)

    mValues = list(map(Multiplication, fValues))
    print("List after Map :", mValues)

    FinalOutput = reduce(Max,mValues)
    print("Final Output is : ", FinalOutput)

if __name__ == "__main__":
    main()

    