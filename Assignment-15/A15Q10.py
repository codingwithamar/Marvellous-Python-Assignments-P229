# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A15Q10.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-15\A15Q10.py
# Subject : 10.Write a lambda function using filter() which accepts a list of numbers 
# and returns the count of even numbers.
# Description : Count of Even Number
# =============================================================================

from functools import reduce

def main():
    print("Enter the list of Numbers : ")
    NumList = list(map(int,input().split()))    #map

    FilterList = list(filter(lambda iNumList : iNumList%2 == 0,NumList))     #filter
    print("This is Even Numbers in your List : ", FilterList)

    ReduceNumber = reduce(lambda iNum1, iNum2 : iNum1 + iNum2 ,FilterList)
    print("Addition of even Numbers : ",ReduceNumber)
    print("Count of filter List is : " ,len(FilterList))

if __name__ == "__main__":
    main()
    