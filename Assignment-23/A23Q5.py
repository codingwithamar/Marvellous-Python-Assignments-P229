# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A23Q5.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-23\A23Q5.py
# Subject/Question : 5: Write a program that calculates factorials of multiple 
# numbers simultaneously using multiprocessing.Pool.
# Description : Input Data = [10, 15, 20, 25] 
# Expected Task : For every N, calculate: N!
# Expected Output Format : Process ID : 1240
#                          Input Number : 20
#                          Factorial : 2432902008176640000
# =============================================================================

from multiprocessing import Pool
from multiprocessing import current_process

def Factorial(iValues):
    Sum = 1
    for i in range(1,iValues+1):
        Sum = Sum * i
    print("Process ID : ",current_process().pid)
    print("Input Number : ",iValues)
    print("Factorial : ",Sum)
    print()
    return Sum

def main():
    print("Enter the list of Numbers")
    Values = list(map(int,input().split()))
    print("Your Entered List is : ",Values)

    with Pool(4) as P:
        P.map(Factorial,Values)

if __name__ == "__main__":
    main()

    