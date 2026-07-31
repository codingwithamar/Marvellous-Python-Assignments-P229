# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A23Q2.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-23\A23Q2.py
# Subject/Question : 2: Write a Python program using multiprocessing.Pool to 
# calculate the sum of all odd numbers from 1 to N.
# Description : Input Data = [1000000, 2000000, 3000000, 4000000]
# Expected Task : 
# For each number N, calculate: 1 + 3 + 5 + ... + N 
# Expected Output Format :  Process ID : 1235
#                           Input Number : 1000000
#                           Sum of Odd Numbers : 250000000000
# =============================================================================

from multiprocessing import Pool
from multiprocessing import current_process

def OddSum(Values):
    Sum = 0
    for Value in range(1,Values+1,2):
        Sum += Value
    print("Process ID : ",current_process().pid)
    print("Input Number : ",Values)
    print("Sum of Odd Numbers : ",Sum)
    print()
    return Sum

def main():
    print("Enter the list of Numbers : ")
    Values = list(map(int,input().split()))
    print("You Entered List of Numbers is : ",Values)

    with Pool(4) as P:
        P.map(OddSum,Values)

if __name__ == "__main__":
    main()

