# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A23Q1.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-23\A23Q1.py
# Subject/Question : 1: Write a Python program using multiprocessing.Pool to calculate
# the sum of all even numbers from 1 to N for every number from the given list.
# Description : 
# Input : Data = [1000000, 2000000, 3000000, 4000000]
# Expected Task : For each number N, calculate: 2 + 4 + 6 + ... + N
# Expected Output Format :
#   Process ID : 1234
#   Input Number : 1000000
#   Sum of Even Numbers : 250000500000
# =============================================================================

from multiprocessing import Pool
from multiprocessing import current_process

def SumEven(Values):
    Sum = 0
    for Value in range(2,Values+1,2):
        Sum = Sum + Value
    print("Process ID : ",current_process().pid)
    print("Input Number : ", Values)
    print("Sum of Even Numbers : ",Sum)
    print()
    return Sum

def main():
    print("Enter the list Of numbers : ")
    Values = list(map(int,input().split()))
    print("You Entered List is : ",Values)

    with Pool(4) as p:
        p.map(SumEven,Values)

if __name__ == "__main__":
    main()
    