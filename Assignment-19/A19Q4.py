# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A19Q4.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-19\A19Q4.py
# Subject : 4.Write a program which contains filter(), map() and reduce() in it. 
# Python application which contains one list of numbers. List contains the numbers 
# which are accepted from user. Filter should filter out all such numbers which are even. 
# Map function will calculate its square. Reduce will return addition of all that numbers.
# Description : 
# Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10] 
# List after filter = [2, 4, 4, 2, 8, 10] 
# List after map = [4, 16, 16, 4, 64, 100]
# Output of reduce = 204
# =============================================================================

from functools import reduce

Even = lambda iValues : iValues%2==0

Square = lambda iValues : iValues * iValues

FinalOutput = lambda iValues1, iValues2 : iValues1 + iValues2

def main():
    print("Enter the list of numbers")
    Values = list(map(int,input().split()))
    
    fValues = list(filter(Even,Values))
    print("List After Filter", fValues)

    mValues = list(map(Square,fValues))
    print("List after map", mValues)

    rValues = reduce(FinalOutput,mValues)
    print("Final Output is : ", rValues)

if __name__ == "__main__":
    main()
    