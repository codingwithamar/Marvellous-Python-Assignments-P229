# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A23Q4.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-23\A23Q4.py
# Subject/Question : 
# 4: Write a program that counts how many odd numbers exist between 1 and N.
# Description : Input Data = [1000000, 2000000, 3000000, 4000000] 
# Expected Output Format : Process ID : 1237
#                          Input Number : 1000000
#                          Odd Number Count : 500000
# =============================================================================

from multiprocessing import Pool
from multiprocessing import current_process

def OddCount(Values):
    Count = 0
    for Value in range(1,Values+1,2):
        Count = Count + 1
    print("Process Id : ",current_process().pid)
    print("Input Number : ",Values)
    print("Odd Number Count : ",Count)
    print()
    return Count

def main():
    print("Enter the list of Numbers")
    Values = list(map(int,input().split()))
    print("You Entered number of list is : ",Values)

    with Pool(4) as P:
        Result = P.map(OddCount,Values)
        
if __name__ == "__main__":
    main()

    