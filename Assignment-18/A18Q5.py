# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A18Q5.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-18\A18Q5.py
# Subject : Write a program which accept N numbers from user and store it into List. Return 
# addition of all prime numbers from that List. Main python file accepts N numbers from user 
# and pass each number to ChkPrime() function which is part of our user defined module named 
# as MarvellousNum. Name of the function from main python file should be ListPrime().
# Description : Input Elements : 13 5 45 7 4 56 10 34 2 5 8
#               Output : 54 (13 + 5 + 7 +2 + 5)
# =============================================================================

import ChkPrime
from functools import reduce

def main():
    print("Enter the list of Numbers :")
    Values = list(map(int,input().split()))
    
    print("Your Entered Number List is : ",Values)
    PrimeNumbers = list(filter(ChkPrime.CheckPrime,Values))
    print("Prime Numbers List : ",PrimeNumbers)

    PrimeAdd = reduce(ChkPrime.PrimeAddition,PrimeNumbers)
    print("Addition Of Prime Numbers is : ",PrimeAdd)

if __name__ == "__main__":
    main()
    