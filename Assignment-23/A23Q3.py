# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A23Q3.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-23\A23Q3.py
# Subject/Question : 3: Write a program that counts how many even numbers exist
# between 1 and N using Pool.map().
# Description : Input Data = [1000000, 2000000, 3000000, 4000000] 
# Expected Output Format :
#                 Process ID : 1236 
#                 Input Number : 1000000 
#                 Even Number Count : 500000

# =============================================================================

from multiprocessing import Pool
from multiprocessing import current_process

def EvenCount(Values):
    Count = 0
    for Value in range(2,Values+1,2):
        Count = Count + 1
    print("Process Id : ",current_process().pid)
    print("Input Number : ",Values)
    print("Even Number Count : ",Count)
    print()
    return Count

def main():
    print("Enter the list of Numbers")
    Values = list(map(int,input().split()))
    print("You Entered number of list is : ",Values)

    with Pool(4) as P:
        Result = P.map(EvenCount,Values)
        
if __name__ == "__main__":
    main()
    